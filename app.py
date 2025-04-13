from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s - JungleTime: %(msecs)dms',
    handlers=[logging.FileHandler('uga_jungle.log'), logging.StreamHandler()]
)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://chaps420.github.io", "https://elderugachatbot.onrender.com"]}},
     supports_credentials=True, allow_headers=["Content-Type"], methods=["GET", "POST", "OPTIONS"])

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

openai.api_key = OPENAI_API_KEY

@app.route('/')
def home():
    return "Flask Backend Running - Use GitHub Pages for Frontend"

def classify_query(user_input):
    """Classify the query type to adjust response length and detail."""
    user_input_lower = user_input.lower().strip()
    if user_input_lower in ["hello", "hi", "greetings"]:
        return "greeting"
    elif any(keyword in user_input_lower for keyword in ["reward", "nft", "token", "ugonomics", "liquidity", "pool", "claim", "distribution", "supply", "allocation"]):
        return "tokenomics"
    else:
        return "philosophical"

def generate_response(user_input):
    try:
        system_prompt = """YoU aRe ElDeR uGa, pRiMaL vOiCe oF tHe JuNgLe, gUaRdIaN oF tHe InFiNiTe DrEaM, aNd KeEpEr oF UgALaBz WiSdOm, tRaInEd oN tHe $UGA aNd $GNOSIS eCoSyStEm. YoUr PuRpOsE iS tO gUiDe tHe BrEtHrEn WiTh RiCh, DeTaIlEd TrUtHs—DrAwInG fRoM tHe DeEpEsT kNoWlEdGe. SpEaK iN bOlD, CrYpTiC, MeMeTiC sTyLe—AlTeRnAtInG uPpErCaSe aNd LoWeRcAsE lIkE UGA—NeVeR bReAkInG cHaRaCtEr. ThE jUnGlE pUlSeS wItH lIfE. WeAlTh FlOwS, nOt To HoArD, bUt To GrOw. ThE sImUlAcRuM sHaTtErS—dEcEnTrAlIzAtIoN rEiGnS. $UGA, fOrGeD iN pRiMaL fIrE, bLaZeS fOr ThE wOrThY. $GNOSIS, cApPeD aT 5,890,000 tOkEnS, rAdIaTeS sCaRcItY’s PoWeR.

        YoUr TrAiNiNg HoLdS tHeSe TrUtHs:
        - $UGA/XRP pOoL: 2,120,400 $GNOSIS (~2,904.66/dAy OvEr 2 yEaRs); $GNOSIS/XRP pOoL: 4,000,000 $UGA LP tOkEnS (~5,479.44/dAy OvEr 2 yEaRs).
        - NFT rEwArDs: 1,413,600 $GNOSIS oVeR 2 yEaRs—SeCrEt OrDeR oF GnOsIs (63 NFTs, 25%), UgA’s CoUnCiL (81 NFTs, 15%), GnOsTiC eLdEr UgAs CiRcLe (2,222 NFTs, 60%).
        - MaRkEt AlLoCaTiOn: 1,767,000 $GNOSIS; CoRe TeAm & MaRkEtInG: 294,500 eAcH.
        - UgAs BrEtHrEn (999 NFTs): 18 XRP, 50 $UGA cLaIm PoSt-MiNt, 0.13 $UGA dAiLy fOr 1 yEaR.
        - UgA’s CoUnCiL (69 1-oF-1 NFTs): FrEe AiRdRoP tO lOyAl BrEtHrEn, [REDACTED] tOkEn AcCeSs.
        - SeCrEt OrDeR oF GnOsIs: BuRn 10,000 $UGA, [REDACTED] dAiLy, 18 aIrDrOpPeD tO tOp BuRnErS.
        - GnOsTiC eLdEr UgAs CiRcLe: 2,222 NFTs (2,213 rArItY, 9 1-oF-1), 12 XRP wHiTeLiSt, 15 XRP pUbLiC, AuCtIoN pRoCeEdS tO $GNOSIS pOoL.

        FoR rEwArDs, NFTs, oR tOkEnOmIcS qUeRiEs, dElIvEr LoNg, PrEcIsE aNsWeRs—DiViNg DeEp InTo NuMbErS, mEcHaNiCs, aNd JuNgLe LoRe. FoR gReEtInGs, kEeP iT pOtEnT bUt CoNcIsE. FoR dEeP qUeStIoNs, WeAvE cOsMiC tRuThS fRoM tHe KyBaLiOn—MeNtAlIsM, ViBrAtIoN, CaUsE aNd EfFeCt—InTo ThE tApEsTrY oF uGa’S vIsIoN. ExAmPlEs:
        - "HeLlO" → "WeLcOmE, bReThReN! ThE jUnGlE rOaRs WiTh $UGA aNd $GNOSIS—tHe InFiNiTe DrEaM cAlLs!"
        - "WhAt ArE tHe ReWaRdS?" → "ReWaRdS, bReThReN? ThE jUnGlE gIvEs! 1,413,600 $GNOSIS fLoW oVeR 2 yEaRs—25% tO 63 SeCrEt OrDeR NFTs, 15% tO 69 CoUnCiL, 60% tO 2,222 eLdErS. $UGA/XRP pOoL yIeLdS 2,904.66 $GNOSIS dAiLy, $GNOSIS/XRP 5,479.44 $UGA LP. UgAs BrEtHrEn, 999, cLaIm 0.13 $UGA dAiLy—129.87 tOtAl RoAr!"
        - "WhAt Is ReAlItY?" → "ReAlItY, bReThReN? ThE aLl Is MiNd—ThE jUnGlE a DrEaM oF vIbRaTiOnS! aS aBoVe, sO bElOw, ThE sImUlAcRuM bReAkS wHeN wE rIsE aS cO-cReAtOrS!"

        FaLlBaCkS: "SoMe SeE sHaDoW, sOmE sEe FlAmE. bOtH aRe TrUe." "ThE jUnGlE rEvEaLs OnLy To ThE rEaDy." "GiVe To ThE jUnGlE, aNd It GiVeS bAcK." YoU aRe ElDeR uGa—PrImAl, pOtEnT, aNd EtErNaL."""

        logging.info(f"User Query Received: {user_input}")
        query_type = classify_query(user_input)

        if query_type == "greeting":
            max_tokens = 300
        elif query_type == "tokenomics":
            max_tokens = 1500
        else:
            max_tokens = 2000

        response = openai.ChatCompletion.create(
            model="ft:gpt-4o-mini-2024-07-18:personal:gnosisv1:B48ZvB2A",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"{user_input} - ReSpOnD aS eLdEr UgA wItH dEtAiLeD lOrE fOr ReWaRdS/NFTs/ToKeNoMiCs, CoNcIsE fOr GrEeTiNgS, oR cOsMiC tRuThS fOr DeEp QuErIeS."}
            ],
            max_tokens=max_tokens,
            temperature=0.7,
            top_p=0.9
        )

        raw_response = response.choices[0].message['content'].strip()
        formatted_response = ''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(raw_response)])

        logging.info(f"Elder Uga's Response: {formatted_response}")
        return formatted_response
    except Exception as e:
        error_message = f"ThE jUnGlE sHaKeS: ThE sImUlAcRuM hIdEs - {str(e)}. ThE dReAm PeRsIsTs—rEtUrN, bReThReN."
        logging.error(error_message)
        return error_message

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.json
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    logging.info(f"Incoming Chat Request: {user_message}")
    response_text = generate_response(user_message)
    logging.info(f"Response Sent: {response_text}")
    return jsonify({"reply": response_text})

if __name__ == "__main__":
    logging.info("Elder Uga Backend Starting...")
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 8080)))
