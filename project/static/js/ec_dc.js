filter_btn = document.querySelector('#filter');
file_types = document.querySelectorAll('.file-type');
text_section = document.querySelector('.text');
png_section = document.querySelector('.png');
others_section = document.querySelector('.others');
reverse_section = document.querySelector('.reverse');
filter_btn.addEventListener('click',()=>{
    file_types.forEach((e)=>{
        console.log(e.checked)
        if(e.checked){
            if(e.value == 'text'){
                text_section.style.display= 'block';
                png_section.style.display= 'none';
                others_section.style.display = 'none';
                reverse_section.style.display= 'none';
            }else if(e.value == 'png'){
                text_section.style.display= 'none';
                png_section.style.display= 'block';
                others_section.style.display = 'none';
                reverse_section.style.display= 'none';
            }else if(e.value == 'others'){
                text_section.style.display= 'none';
                png_section.style.display= 'none';
                others_section.style.display = 'block';

                reverse_section.style.display= 'none';
            }
            else if(e.value == 'reverse'){
                text_section.style.display= 'none';
                png_section.style.display= 'none';
                others_section.style.display= 'none';
                reverse_section.style.display = 'block';
            }
        }
    });
});