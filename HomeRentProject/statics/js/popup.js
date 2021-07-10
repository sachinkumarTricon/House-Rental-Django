var csrftoken = undefined;
function getCookie(name) {
     var cookieValue = null;
     if (document.cookie && document.cookie !== '') {
         var cookies = document.cookie.split(';');
         for (var i = 0; i < cookies.length; i++) {
             var cookie = cookies[i].trim();
             // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                   break;
            }
         }
     }
     return cookieValue;

}
document.addEventListener("DOMContentLoaded", function(event) {

      csrftoken = getCookie('csrftoken');
  });


// For Verify Phone Pop up API CALL

var phoneVerifyform = document.getElementById('verifyPhoneform')
phoneVerifyform.addEventListener('submit', function(e){
    e.preventDefault()
    console.log('Clicked on OTP Generate...')
    verifyPhone()
//    document.getElementById('form-button').classList.add("hidden");

})
    var verifyPhoneData = {

        'phone':null,

    }

function verifyPhone(){

//    var userFormData = {
//        'name':null,
//        'email':null,
//        'total':total,
//    }



        verifyPhoneData.phone = phoneVerifyform.phone.value



//    console.log('verifyphone data  :', verifyPhoneData)

    var url = "http://127.0.0.1:8000/api/validatePhone"
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'applicaiton/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify(verifyPhoneData),

    })
    .then((response) => response.json())
    .then((data) => {
        if (data.status){
           console.log("ye return aaya hai basckend se ",data)
           document.getElementById('verifyPhoneClose').click()
           $("#verifyOTPModal").modal()
        }
        else{
             window.location.href = "/rent/home"
        }

    })
}



// For Verify OTP Pop up API CALL

var otpform = document.getElementById('verifyotpform')
otpform.addEventListener('submit', function(e){
    e.preventDefault()
    console.log('Clicked on VerifyOTP...')
    verifyOTP()
//    document.getElementById('form-button').classList.add("hidden");

})


function verifyOTP(){

//    var userFormData = {
//        'name':null,
//        'email':null,
//        'total':total,
//    }

    var verifyOTPData = {

        'otp':null,
        'phone': verifyPhoneData.phone


    }


        verifyOTPData.otp = otpform.otp.value

    var url = "http://127.0.0.1:8000/api/validateOTP"
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'applicaiton/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify(verifyOTPData),

    })
    .then((response) => response.json())
    .then((data) => {
        if (data.status){
           console.log(data)
           document.getElementById('verifyOTPClose').click()
           $("#regModal").modal()
        }
        else{
          alert("OTP does not Matched try again")
          window.location.href = "/rent/home"
        }



    })
}



// register API call



var regform = document.getElementById('myform')
regform.addEventListener('submit', function(e){
    e.preventDefault()
    console.log('Clicked on register ...')
    register()
//    document.getElementById('form-button').classList.add("hidden");

})


function register(){

    var userFormData = {
        'username':null,
        'email':null,
        'DOB':null,
        'password':null,
        'phone': verifyPhoneData.phone
    }


        userFormData.username = regform.full_name.value
        userFormData.email = regform.your_email.value
        userFormData.DOB = regform.dob.value
        userFormData.password = regform.password.value




    console.log('userFormData ka  data  :', userFormData)

    var url = "http://127.0.0.1:8000/api/register"
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'applicaiton/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify(userFormData),

    })
    .then((response) => response.json())
    .then((data) => {
        if (data.status){
           console.log(data)
           document.getElementById('CloseRegModal').click()
        }
        else{
          console.log(data)
          alert("Registration failed ")
          window.location.href = "/rent/home"
        }



    })
}

// Login API Call

var loginform = document.getElementById('loginform')

loginform.addEventListener('submit', function(e){
    e.preventDefault()
    console.log('Clicked on VerifyOTP...')
    login()
//    document.getElementById('form-button').classList.add("hidden");

})
var loginformData = {
        'password':null,
        'phone': null
    }

var Auth_Token

function login(){

    loginformData.password = loginform.passwd.value
    loginformData.phone = loginform.phn.value

    var url = "http://127.0.0.1:8000/api/login"
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'applicaiton/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify(loginformData),

    })
    .then((response) => response.json())
    .then((data) =>checkstatus(data))



     function checkstatus(data){
        console.log(data.status)
        if (data.status){
            Auth_Token = data.token
            localStorage.setItem('Auth_Token',Auth_Token)
            console.log("ye auth token hai login wala : ",Auth_Token)
            window.location.href = "/rent/home"
        }
        else{
          alert("something went wrong ")
          window.location.href = "/rent/home"
        }

     }


}

