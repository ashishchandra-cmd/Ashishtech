function displayphone()
{
    
    var pnumber = document.getElementById("id_phone").value;
    var param = 'cname='+pnumber;
    var req = new XMLHttpRequest();
    req.onreadystatechange = show;
    req.open("POST","http://127.0.0.1:8000/phoneurl/",true);
    req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    req.send(param);
       
     function show()
               {  
                if(req.readyState == 4)
                       {
                         var v = req.responseText;
                         var json_data = JSON.parse(v);  
                          if(json_data.error=='phone number taken'){
                            document.getElementById('sp_phone').innerText =json_data.error;
                            document.getElementById('b1').disabled=true;
                               }
                          
                          else{
                            document.getElementById('sp_phone').innerText = json_data.message;
                            document.getElementById('b1').disabled=false;
                          }
                       }
               }
  }

