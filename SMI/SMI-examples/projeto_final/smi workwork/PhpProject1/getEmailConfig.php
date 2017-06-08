<?php

  $ligacao;
  $configDataBase;
  $configDataFiles;
  $username;
  $password;

function getEmailConfigurations(){

    global $configDataBase;
    global $configDataFiles;
    global $username;
    global $password;

    $configFile = "../account_smi_mail/acc.xml";

    if ( ($configDataBase==NULL)) {
        ($aux = simplexml_load_file( $configFile )) or die ("Can't read configuration file.");
        $configDataBase = $aux[0];
        $username     = $configDataBase->user;
        $password     = $configDataBase->password;
      }
}

function getEmailDomain($email){
    $array= explode("@", $email);
    $array = explode(".",$array[1]);
    return $array[0];
}

?>
