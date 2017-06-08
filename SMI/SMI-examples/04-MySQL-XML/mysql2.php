<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
    <title>MySQL - Example 2</title>
    
    <link REL="stylesheet" TYPE="text/css" href="../Styles/GlobalStyle.css">
  </head>
  
  <body>
    <?php
      $linkIdentifier = mysqli_connect( "localhost:3306", "smi", "segredo" );
      
      mysqli_set_charset($linkIdentifier, 'utf8');

      mysqli_select_db($linkIdentifier, "smi");

      $query = 
              "INSERT INTO `email-accounts` " .
              "(`accountName`, `smtpServer`, `port`, `timeout`, `loginName`, `email`, `displayName`) values " .
              "('ISEL-2', 'mail.isel.pt', '587', '30', 'd1371', 'd1371@deetc.isel.pt', 'Carlos Gonçalves')";
      mysqli_query($linkIdentifier, $query);

      $recordsInserted = mysqli_affected_rows( $linkIdentifier );
    
      if ( $recordsInserted==-1 ) {
        echo "Insert has failed!";
      }
      else {
        echo "Account added with success.";
      }
      mysqli_close( $linkIdentifier );
    ?>
  </body>
</html>