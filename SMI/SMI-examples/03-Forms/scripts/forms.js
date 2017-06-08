// Validate the login form
function FormLoginValidator(theForm) {
  // Check to see if name isn't blank
  if ( (theForm.name.value === "") || (theForm.name.value === "Type your name") ) {
    alert("You must enter a name.");
    theForm.name.focus();
    return false;
  }

  // Check to see if e-mail isn't blank and is well formed
  // Read more at http://www.marketingtechblog.com/javascript-regex-emailaddress/#ixzz1p1ZDMNZe
  var filter;
  filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,3})$/;
  //filter = /^([a-z0-9_\.\-])+\@(([a-z0-9\-])+\.)+([a-z0-9]{2,4})$/i;
  if ( !filter.test( theForm.email.value ) ) {
    alert('Please provide a valid e-mail address');
    theForm.email.focus();
    return false;
  }

  return true;
}

function FormUpdateProfileValidator(theForm) {
  alert( 'Home work for the students!' );
  return true;
  //return false;
}

var xmlHttp;

function GetXmlHttpObject() {
  try {
    return new ActiveXObject("Msxml2.XMLHTTP");
  } catch(e) {} // Internet Explorer
  try {
    return new ActiveXObject("Microsoft.XMLHTTP");
  } catch(e) {} // Internet Explorer
  try {
    return new XMLHttpRequest();
  } catch(e) {} // Firefox, Opera 8.0+, Safari
  alert("XMLHttpRequest not supported");
  return null;
}

// The District Select has change
function SelectDistrictChange(theSelect) {
  // The new option
  var selectedDistrict = theSelect.value;

  // The new image to display
  var districtImageFile = "images/distritos/" + selectedDistrict + ".gif";
  document.getElementById("imgDistrict").src = districtImageFile;

  // Preparing the arguments to request the counties
  var args = "district="+selectedDistrict;

  // With HTTP GET method
  xmlHttp = GetXmlHttpObject();
  xmlHttp.open("GET", "getCounties.php?"+args, true);
  xmlHttp.onreadystatechange=SelectDistrictHandleReply;
  xmlHttp.send(null);
}

//Fill in the counties for the new district
function SelectDistrictHandleReply() {

  //alert( xmlHttp.readyState );

  if( xmlHttp.readyState === 4 ) {
    var countySelect=document.getElementById("county");

    countySelect.options.length = 0;

    var countiesRaw = xmlHttp.responseText;

    //alert(countiesRaw);

    var counties = countiesRaw.split("@");

    for (i=0; i<counties.length; i++) {

      var currentCounty = counties[i].split("|");
      var value  = currentCounty[0];
      var option = currentCounty[1];

      try{
        countySelect.add( new Option("", value), null);
      }
      catch(e) {
        countySelect.add( new Option("", value));
      }

      countySelect.options[i].innerHTML = option;
    }
  }
}

//The County Select has change
function SelectCountyChange(theSelect) {
  // The new option
  var selectedCounty = theSelect.value;

  // Preparing the arguments to request the counties
  var args = "county="+selectedCounty;

  xmlHttp = GetXmlHttpObject();
  xmlHttp.open("GET", "getZips.php?"+args, true);
  xmlHttp.onreadystatechange=SelectCountyHandleReply;
  xmlHttp.send( null );
}

//Fill in the Zips for the new county
function SelectCountyHandleReply() {

  if( xmlHttp.readyState === 4 ) {
    var zipSelect=document.getElementById("zip");

    for(var count = zipSelect.options.length - 1; count >= 0; count--) {
      zipSelect.options[count] = null;
    }

    var zipsRaw = xmlHttp.responseText;

    var zips = zipsRaw.split("@");
    for (i=0; i<zips.length; i++) {

      var currentZip = zips[i].split("|");
      //codigo postal
      var value  = currentZip[0];
      //nome da localização
      var option = currentZip[1];

      try{
        zipSelect.add( new Option(option, value), null);
      }
      catch(e) {
        zipSelect.add( new Option(option, value) );
      }
    }
  }
}
