<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
    <title>Hello World</title>
    
    <link REL="stylesheet" TYPE="text/css" href="../Styles/GlobalStyle.css">
  </head>
  <body>    
<?php
  if ( isset( $_SERVER[ 'REMOTE_ADDR' ] ) ) {
    $browserAddress = $_SERVER[ 'REMOTE_ADDR' ];
  }
  else {
    $browserAddress = "N.A.";
  }
  
  if ( isset( $_SERVER[ 'REMOTE_HOST' ] ) ) {
    $browserHost = $_SERVER[ 'REMOTE_HOST' ];
  }
  else {
    $browserHost = "N.A.";
  }
  
  if ( isset( $_SERVER[ 'SERVER_NAME' ] ) ) {
    $serverName = $_SERVER[ 'SERVER_NAME' ];
  }
  else {
    $serverName = "N.A.";
  }

  echo "<p>Hello. Yor are viewing this page from $browserHost ($browserAddress) generated @ $serverName</p>";
  
  echo "<p>To get the fully qualified name for the Apache Web server modify the following tags:</p>\n";
  
  echo "<code>ServerName MyServerName</code> in \"httpd.conf\" file +/- line 219\n<br>";
  echo "<code>UseCanonicalName On</code> in \"extra/httpd-default\" file +/- line 38\n<br>";
?>

  <br>
  <br>
  <a href="../index.php">Back to Examples Pages</a>

  </body>
</html>