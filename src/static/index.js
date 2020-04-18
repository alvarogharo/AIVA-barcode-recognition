const SERVER_URL = "http://localhost";
const SERVER_PORT = "8100";

const FILE_INPUT_ID = "fileInput";
const RESULT_TEXT_ID = "resultText";
const PREVIEW_IMAGE_ID = "previewImage";
const IMAGE_DIV_ID = "imageDiv";

const BASE64_SPLIT_CHAR = ",";

const IMAGE_JSON_KEY = "img";
const RESULT_JSON_KEY = "result";

const QUERY_RECOGNIZE = "/recognize";
const METHOD_POST = "POST";

const ATTRIB_SRC = "src";

const EMPTY_SRC_VALUE = "#";

const TYPE_TIFF = "image/tiff";

const toBase64 = file => new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = error => reject(error);
});

function onImageChange(input) {
    let file;
    let previewImage = document.getElementById(PREVIEW_IMAGE_ID);
    let div = document.getElementById(IMAGE_DIV_ID);
    div.innerHTML = "";
    const reader = new FileReader();
    reader.onload = (e) => {
        if (file.type === TYPE_TIFF) {
            let tiff = new Tiff({buffer: e.target.result});
            var canvas = tiff.toCanvas();
            previewImage.setAttribute(ATTRIB_SRC, EMPTY_SRC_VALUE);
            div.append(canvas);
        } else {
            previewImage.setAttribute(ATTRIB_SRC, e.target.result);
        }
    };
    file = input.files[0];
    if (file.type === TYPE_TIFF) {
        reader.readAsArrayBuffer(file);
    } else {
        reader.readAsDataURL(file);
    }
}

async function sendAndRecognize() {
    let file = document.getElementById(FILE_INPUT_ID).files[0]
    let base64File = await toBase64(file);
    base64File = base64File.split(BASE64_SPLIT_CHAR)[1];
    let data = {};
    data[IMAGE_JSON_KEY] = base64File;
    let json = JSON.stringify(data);
    console.log(base64File);
    let xhr = new XMLHttpRequest();
    xhr.open(METHOD_POST, SERVER_URL + ":" + SERVER_PORT + QUERY_RECOGNIZE, true);
    xhr.setRequestHeader('Content-type','application/json; charset=utf-8');
    xhr.onload = function () {
        let resultText = document.getElementById(RESULT_TEXT_ID);
        let result = JSON.parse(xhr.responseText)[RESULT_JSON_KEY];
        resultText.innerText = result;
        console.log("Decoded result is: " + result);
    }
    xhr.send(json);
}
