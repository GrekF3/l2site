if ($('.tinymce').length) {
    tinymce.activeEditor.destroy();
}

tinymce.init({
    elements: "id_content",
    selector: "textarea#id_content",
    height: "700",
    width: "100%", menubar: "file edit view insert format tools table help",
    plugins: "media image preview advlist autolink lists link  charmap print preview anchor searchreplace visualblocks code fullscreen insertdatetime media table paste code help wordcount spellchecker",
    toolbar: "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment code",
    image_title: true,
    image_caption: true,
    automatic_uploads: true,
    image_advtab: true,
    language: "ru",
    file_picker_types: "image media",
     // обработчик загрузчика файла
    file_picker_callback: function (cb, value, meta) {
        var input = document.createElement("input");
        input.setAttribute("type", "file");
        if (meta.filetype == "image") {
            input.setAttribute("accept", "image/*");
        }
        if (meta.filetype == "media") {
            input.setAttribute("accept", "video/*");
        }
        input.onchange = function () {
            var file = this.files[0];
            var reader = new FileReader();
            reader.onload = function () {
                var id = "blobid" + (new Date()).getTime();
                var blobCache = tinymce.activeEditor.editorUpload.blobCache;
                var base64 = reader.result.split(",")[1];
                var blobInfo = blobCache.create(id, file, base64);
                blobCache.add(blobInfo);
                cb(blobInfo.blobUri(), {title: file.name});
            };
            reader.readAsDataURL(file);
        };
        input.click();
    },
    content_style: "body { font-family:Helvetica,Arial,sans-serif; font-size:14px }"
});