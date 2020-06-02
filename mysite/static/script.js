//функция валидации для формы регистрации
function handleButtonClick() {
  
   var textInput = document.getElementById("name");
      if(textInput.value == ""){
        document.getElementById("divname").innerHTML="Введите Ваше имя, пожалуйста.";
        //alert("Введите Ваше имя, пожалуйста");
        document.callback.name.focus();
        return false;
    }
    var rename = /^[A-ZА-Я]+[a-zа-я]{1,20}/u;
    if(!rename.test(textInput.value)){
        document.getElementById("divname").innerHTML="Имя должно начинаться с заглавной буквы.";
        //alert("Имя должно начинаться с заглавной буквы ");
        document.callback.name.focus();
        return false;
    }
    
    var relastname = /^[A-ZА-Я]+[a-zа-я]{1,20}/u;
    if(!relastname.test(textInput.value)){
        document.getElementById("divlastname").innerHTML="Фамилия должна начинаться с заглавной буквы.";
        //alert("Фамилия должна начинаться с заглавной буквы ");
        document.callback.name.focus();
        return false;
    }
    
    var textInput = document.getElementById("phone");
      if(textInput.value == ""){
        document.getElementById("divphone").innerHTML="Введите номер телефона, пожалуйста.";
        //alert("Введите номер телефона, пожалуйста");
        document.callback.name.focus();
        return false;
    }
    var rephone = /^\d[\d\(\)\ -]{4,11}\d$/;
    if(!rephone.test(textInput.value)){
        document.getElementById("divphone").innerHTML="Номер телефона должен быть длиной 5-11 символов.";
        //alert("Номер телефона должен быть длиной 5-11 символов");
        document.callback.name.focus();
        return false;
    }
   
    var textInput = document.getElementById("city");
      if(textInput.value == ""){
        document.getElementById("divcity").innerHTML="Введите город, пожалуйста.";
        //alert("Введите город, пожалуйста");
        document.callback.name.focus();
        return false;
    }
    var rename = /^[A-ZА-Я]+[a-zа-я]{1,20}/u;
    if(!rename.test(textInput.value)){
        document.getElementById("divcity").innerHTML="Название города должно начинаться с заглавной буквы.";
        //alert("Название города должно начинаться с заглавной буквы");
        document.callback.name.focus();
        return false;
    }
    
    var textInput = document.getElementById("inputEmail4");
      if(textInput.value == ""){
        document.getElementById("divmail").innerHTML="Введите адрес электронной почты, пожалуйста.";
        //alert("Введите адрес электронной почты, пожалуйста");
        document.callback.name.focus();
        return false;
    }
    var remail = /^[\w-\.]+@[\w-]+\.[a-z]{2,4}$/i;
    if(!remail.test(textInput.value)){
        document.getElementById("divmail").innerHTML="Введите адрес электронной почты корректно, например, book12@mail.ru";
        //alert("Введите адрес электронной почты корректно, например, book12@mail.ru");
        document.callback.name.focus();
        return false;
    }
    
    var passInput = document.getElementById("inputPassword");
      if(passInput.value == ""){
        document.getElementById("divpassword").innerHTML="Введите пароль, пожалуйста.";
        //alert("Введите пароль, пожалуйста");
        document.callback.name.focus();
        return false;
    }
      var letter = document.getElementById("letter");
      var capital = document.getElementById("capital");
      var number = document.getElementById("number");
      var length = document.getElementById("length");
      // Проверка на строчные буквы
       var lowerCaseLetters = /[a-zа-я]/g;
        if(passInput.value.match(lowerCaseLetters)) {  
          letter.classList.remove("invalid");
          letter.classList.add("valid");
        } else {
          letter.classList.remove("valid");
          letter.classList.add("invalid");
        }  
        // Проверка на заглавные буквы
        var upperCaseLetters = /[A-ZА-Я]/g;
        if(passInput.value.match(upperCaseLetters)) {  
          capital.classList.remove("invalid");
          capital.classList.add("valid");
        } else {
          capital.classList.remove("valid");
          capital.classList.add("invalid");
        }
        // Проверка на цифры
        var numbers = /[0-9]/g;
        if(passInput.value.match(numbers)) {  
          number.classList.remove("invalid");
          number.classList.add("valid");
        } else {
          number.classList.remove("valid");
          number.classList.add("invalid");
        }  
        // Проверка на длину
        if(passInput.value.length >= 8) {
          length.classList.remove("invalid");
          length.classList.add("valid");
        } else {
          length.classList.remove("valid");
          length.classList.add("invalid");
        }

    var confpassInput = document.getElementById("inputPasswordConfirmation");
      if(confpassInput.value == ""){
        document.getElementById("divconfpass").innerHTML="Подтвердите пароль, пожалуйста.";
        //alert("Подтвердите пароль, пожалуйста");
        document.callback.name.focus();
        return false;
    }
    
    if(passInput.value!=confpassInput.value){
      document.getElementById("divconfpass").innerHTML="Пароли не совпадают! Повторите ввод еще раз.";
      document.callback.name.focus();
        return false;
    }
   //document.location.replace("person");
    return true;
}

//валидация для формы входа
function handleButtonClick2() {
    var textInput = document.getElementById("login");
      if(textInput.value == ""){
        document.getElementById("diventerphone").innerHTML="Введите номер телефона, пожалуйста.";
        //alert("Введите номер телефона, пожалуйста");
        document.callback.name.focus();
        return false;
    }
    var rephone = /^\d[\d\(\)\ -]{4,11}\d$/;
    if(!rephone.test(textInput.value)){
        document.getElementById("diventerphone").innerHTML="Номер телефона должен быть длиной 5-11 символов.";
        //alert("Номер телефона должен быть длиной 5-11 символов");
        document.callback.name.focus();
        return false;
    }
    
    var textInput = document.getElementById("passwordenter");
      if(textInput.value == ""){
        document.getElementById("diventerpass").innerHTML="Введите пароль, пожалуйста.";
        //alert("Введите пароль, пожалуйста");
        document.callback.name.focus();
        return false;
    }
    //document.location.replace ("person");
    return true;
}

function like()
{
    var like = $(this);
    var type = like.data('type');
    var pk = like.data('id');
    var action = like.data('action');
    var dislike = like.next();

    $.ajax({
        url : "/inform/" + pk + "/" + action + "/",
        type : 'POST',
        data : { 'obj' : pk },
        success : function (json) {
            like.find("[data-count='like']").text(json.like_count);
            dislike.find("[data-count='dislike']").text(json.dislike_count);
        }
    });
    return false;
}

function dislike()
{
    var dislike = $(this);
    var type = dislike.data('type');
    var pk = dislike.data('id');
    var action = dislike.data('action');
    var like = dislike.prev();

    $.ajax({
        url : "/inform/" + pk + "/" + action + "/",
        type : 'POST',
        data : { 'obj' : pk },
        success : function (json) {
            dislike.find("[data-count='dislike']").text(json.dislike_count);
            like.find("[data-count='like']").text(json.like_count);
        }
    });
    return false;
}

// Подключение обработчиков
$(function() {
    $('[data-action="like"]').click(like())
    $('[data-action="dislike"]').click(dislike());
});
