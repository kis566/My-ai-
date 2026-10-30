"""HUD video player — Mark LIII add-on.

MainWindow ke stack me index 2 pe add hota hai (0=orb, 1=camera, 2=video).
main.py me:
    from hud_video import HudVideoPlayer
    self._hud_video = HudVideoPlayer(self._hud_cam_stack, self._hud_cam_stack.parent())
    self._hud_video.start()
"""

from __future__ import annotations
from pathlib import Path

from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtWidgets import QStackedWidget, QVBoxLayout, QWidget, QSizePolicy


class HudVideoPlayer(QWidget):
    def __init__(self, stack: QStackedWidget, parent=None,
                 video_path: str | Path | None = None, muted: bool = True):
        super().__init__(parent)
        self._stack = stack
        self._path  = Path(video_path) if video_path else None
        self._active = False

        self.setStyleSheet("background: #000308;")
        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        self._vw = QVideoWidget()
        self._vw.setSizePolicy(QSizePolicy.Policy.Expanding,
                               QSizePolicy.Policy.Expanding)
        try:
            self._vw.setAspectRatioMode(
                Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        except Exception:
            pass
        lay.addWidget(self._vw)

        self._player = QMediaPlayer(self)
        self._audio  = QAudioOutput(self)
        self._audio.setVolume(0.0 if muted else 0.5)
        self._player.setAudioOutput(self._audio)
        self._player.setVideoOutput(self._vw)
        self._player.mediaStatusChanged.connect(self._on_status)

        self._stack.addWidget(self)   # index 2

    # ── public ───────────────────────────────────────────────────────────────
    def start(self) -> None:
        if not self._path or not self._path.is_file():
            print(f"[HUD Video] not found: {self._path}")
            return
        self._player.setSource(QUrl.fromLocalFile(str(self._path)))
        self._player.play()
        self._stack.setCurrentIndex(2)
        self._active = True

    def stop(self) -> None:
        self._player.stop()
        self._stack.setCurrentIndex(0)
        self._active = False

    def toggle(self) -> bool:
        self.stop() if self._active else self.start()
        return self._active

    @property
    def is_active(self) -> bool:
        return self._active

    def _on_status(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self._player.setPosition(0)
            self._player.play()