user_photo = document.getElementById('userphoto');
const upload_container = document.querySelector('.upload-contatiner');
const upload_image = document.querySelector('.upload-preview-image');
const fallback_text = document.querySelector('.upload-preview-text');
user_photo.addEventListener('change', function(){
    var file = this.files[0];
    //console.log(file);
    if(file){
        const reader = new FileReader();
        //document.querySelector('.photo-preview').style.display = 'inline';
        upload_container.style.display = 'block';
        fallback_text.style.display = 'none';
        upload_image.style.display = 'block';

        reader.addEventListener("load", function(){
            upload_image.setAttribute("src", this.result);
        });

        reader.readAsDataURL(file);
    }else{
        //document.querySelector('.photo-preview').style.display = null;
        upload_container.style.display = null;
        fallback_text.style.display = null;
        upload_image.style.display = null;
    }
});

document.querySelector('.custom-submit').addEventListener('click',()=>{
    document.querySelector('.submit').click()
})