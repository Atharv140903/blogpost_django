function registerUser(){

    var username = document.getElementById('registerUsername').value
    var password = document.getElementById('registerPassword').value

    var csrf = document.getElementById('csrf').value

    if( username == "" && password == ""){
        alert("Please enter both")
    }

    var data ={
        'username' : username,
        'password' : password

    }

    fetch('/api/register/' , {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrf,
        },
        body : JSON.stringify(data)
    }).then(result => result.json())
      .then(response => {
        
        if(response.status == 200){
            alert(response.message)
        }
        else{
            alert(response.message)
        }
      })


}