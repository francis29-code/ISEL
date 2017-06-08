var xmlHttp;

function GetXmlHttpObject() {
    try {
        return new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {
    } // Internet Explorer
    try {
        return new ActiveXObject("Microsoft.XMLHTTP");
    } catch (e) {
    } // Internet Explorer
    try {
        return new XMLHttpRequest();
    } catch (e) {
    } // Firefox, Opera 8.0+, Safari
    alert("XMLHttpRequest not supported");
    return null;
}

function addAddress(contacts, list) {

    var selectContacts = document.getElementsByName(contacts)[0];
    var contactId = selectContacts.value;

    if (contactId > 0) {
        xmlHttp = GetXmlHttpObject();

        switch (list) {
            case 'toList':
                xmlHttp.open("GET", "getContactDetails.php?contactId=" + contactId, true);
                xmlHttp.onreadystatechange = addressToListReady;
                break;
            case 'ccList':
                xmlHttp.open("GET", "getContactDetails.php?contactId=" + contactId, true);
                xmlHttp.onreadystatechange = addressCcListReady;
                break;
            case 'bccList':
                xmlHttp.open("GET", "getContactDetails.php?contactId=" + contactId, true);
                xmlHttp.onreadystatechange = addressBccListReady;
                break;
        }
        xmlHttp.send(null);
    }
}

function addressToListReady() {
    if (xmlHttp.readyState === 4 && xmlHttp.status === 200) {
        addNewAddress('toList', xmlHttp.responseText);
    }
}

function addressCcListReady() {
    if (xmlHttp.readyState === 4 && xmlHttp.status === 200) {
        addNewAddress('ccList', xmlHttp.responseText);
    }
}

function addressBccListReady() {
    if (xmlHttp.readyState === 4 && xmlHttp.status === 200) {
        addNewAddress('bccList', xmlHttp.responseText);
    }
}

function addNewAddress(list, contactFormated) {
    var input = document.getElementsByName(list)[0];

    if (input.value.length !== 0) {
        input.value = input.value + "; " + contactFormated;
    } else {
        input.value = contactFormated;
    }
}
