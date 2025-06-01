"""
Routes vocales pour l’API Dihya (TTS, ASR, IA, VR, AR)
Sécurité, audit, RGPD, multilingue, plugins IA, WebSocket.
"""

from fastapi import APIRouter, WebSocket, Request, Depends, HTTPException

from backend.security import verify_jwt, get_current_user
from backend.i18n import get_locale_message
from backend.audit import log_audit
from backend.voice import synthesize_speech, recognize_speech

router = APIRouter(prefix="/voice", tags=["voice"])


@router.post(
    "/synthesize",
    summary="Synthèse vocale IA",
    response_model=dict,
)
async def synthesize(
    request: Request,
    data: dict,
    user=Depends(get_current_user),
):
    """
    Synthétise un texte en voix (TTS), multilingue, RGPD, audit.
    """
    log_audit(user, "synthesize", data)
    try:
        audio = synthesize_speech(data["text"], lang=data.get("lang", "fr"))
        return {"audio": audio, "status": "ok"}
    except Exception:
        raise HTTPException(
            status_code=500,
            detail=get_locale_message(request, "internal_error", lang=user.lang),
        )


@router.websocket("/recognize")
async def recognize_ws(websocket: WebSocket):
    """
    WebSocket pour reconnaissance vocale temps réel (ASR).
    """
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_bytes()
            text = recognize_speech(data)
            await websocket.send_json({"text": text})
    except Exception:
        await websocket.close()
