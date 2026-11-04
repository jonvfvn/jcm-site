"""Export the private CV source as a tagged PDF using LibreOffice Writer."""
import json
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

CV = Path(__file__).resolve().parents[1] / "site" / "cv"
BASENAME = "Jonathan-Carson-McGeary-CV"

settings = {
    "UseTaggedPDF": {"type": "boolean", "value": "true"},
    "PDFUACompliance": {"type": "boolean", "value": "true"},
}

with TemporaryDirectory(prefix="jcm-cv-") as directory:
    temp = Path(directory)
    source = temp / f"{BASENAME}.html"
    source.write_bytes(Path(__file__).with_name("cv-source.html").read_bytes())
    subprocess.run(
        [
            "soffice",
            f"-env:UserInstallation={(temp / 'profile').as_uri()}",
            "--headless",
            "--infilter=HTML (StarWriter)",
            "--convert-to",
            f"pdf:writer_pdf_Export:{json.dumps(settings)}",
            "--outdir",
            str(temp),
            str(source),
        ],
        check=True,
    )
    (CV / f"{BASENAME}.pdf").write_bytes(source.with_suffix(".pdf").read_bytes())
