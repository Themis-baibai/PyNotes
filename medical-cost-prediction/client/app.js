function getChildrenValue() {
  var uiChildren = document.getElementsByName("uiChildren");
  for(var i in uiChildren) {
    if(uiChildren[i].checked) {
        return parseInt(i);
    }
  }
  return -1; // Invalid Value
}

function getSmokeValue() {
  var uiSmoke = document.getElementsByName("uiSmoke");
  for(var i in uiSmoke) {
    if(uiSmoke[i].checked) {
        return parseInt(i);
    }
  }
  return -1; // Invalid Value
}

function getGenderValue() {
  var uiGender = document.getElementsByName("uiGender");
  for(var i in uiGender) {
    if(uiGender[i].checked) {
        return parseInt(i);
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
 var age = document.getElementById("uiAge");
  var bmi = document.getElementById("uiBmi");
  var gender = getGenderValue();
  var smoke = getSmokeValue();
  var children = getChildrenValue();
  var region = document.getElementById("uiRegion");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_medical_charge";
  //var url = "/api/predict_medical_charge"

  $.post(url, {
      region: region.value,
      age: age.value,
      sex: gender,
      bmi: bmi.value,
      children: children,
      smoker: smoke,
      
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " USD</h2>";
      console.log(status);
  });
}


function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/get_region";
  //var url = "/api/get_region"
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var region = data.region;
          var uiRegion = document.getElementById("uiRegion");
          $('#uiRegion').empty();
          for(var i in region) {
              var opt = new Option(region[i]);
              $('#uiRegion').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;
  
  