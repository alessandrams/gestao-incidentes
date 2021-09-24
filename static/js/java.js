var incident_types = ['incidente-interno', 'site-malicioso', 'abuso-site', 'acesso-nao-autorizado', 'distribuicao-info', 'phishing', 'malware-virus', 'ransonware', 'ddos', 'arquivo-suspeito', 'atividade-rede', 'outros']

var sel = document.getElementById('incident_type');    
    sel.onchange = function(){ 
      if (sel.value == "1"){
        incident_types.forEach(function(item){ 
          document.getElementById(item).style.display = "none";
          console.log(item)
        });  
        document.getElementById('incidente-interno').style.display = "block";
      }
      if (sel.value == "2"){
        document.getElementById('site-malicioso').style.display = "block";
      }
      if (sel.value == "3"){
        document.getElementById('abuso-site').style.display = "block";
      }
      if (sel.value == "4"){
        document.getElementById('acesso-nao-autorizado').style.display = "block";
      }
      if (sel.value == "5"){
        document.getElementById('distribuicao-info').style.display = "block";
      }
      if (sel.value == "6"){
        document.getElementById('phishing').style.display = "block";
      }
      if (sel.value == "7"){
        document.getElementById('malware-virus').style.display = "block";
      }
      if (sel.value == "8"){
        document.getElementById('ransonware').style.display = "block";
      }
      if (sel.value == "9"){
        document.getElementById('ddos').style.display = "block";
      }
      if (sel.value == "10"){
        document.getElementById('arquivo-suspeito').style.display = "block";
      }
      if (sel.value == "11"){
        document.getElementById('atividade-rede').style.display = "block";
      }
      if (sel.value == "12"){
        document.getElementById('outros').style.display = "block";
      }
    }