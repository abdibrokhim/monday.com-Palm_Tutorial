import PyPDF2
import vertexai
from vertexai.language_models import TextGenerationModel


def download_pdf(url, file_name):
    import requests

    r = requests.get(url, stream=True)

    with open(file_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    return file_name


def read_pdf(file) -> str:
    _data = ""

    pdfReader = PyPDF2.PdfReader(file)

    pages = len(pdfReader.pages)

    for i in range(pages):

        page = pdfReader.pages[i]

        t = page.extract_text()

        _data += t

    return _data


def get_response(query, file_path):

    d_pdf = download_pdf(file_name="test.pdf", url=file_path)

    _pdf = read_pdf(d_pdf)

    vertexai.init(project="your_project_id", location="us-central1")

    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40
    }

    model = TextGenerationModel.from_pretrained("text-bison@001")

    response = model.predict(
        _pdf + '\n\n' + query,
        **parameters
    )

    print(f"Response from Model: {response.text}")

    return response.text



