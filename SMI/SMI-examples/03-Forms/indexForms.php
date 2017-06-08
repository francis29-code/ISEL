<!DOCTYPE html>
<?php
  require_once("../Lib/lib.php");

  $browser = getBrowser();
  
  if ($browser == "Mobile Device") {
    header( 'Location: formLoginSmall.php');
  }
  else {
    header('Location: formLoginBig.php');
  }
?>
