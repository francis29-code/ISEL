<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
    <title>Process login - Forms App</title>
  </head>

  <body>  
    <?php
    $method = $_SERVER[ 'REQUEST_METHOD' ];

    if ( $method=='POST') {
      $args = $_POST;
    } elseif ( $method=='GET' ) {
      $args = $_GET;
    }
    else {
      $args = null;
      
      echo "Invalid HTTP method (" . $method . ")";
      exit();
    }

    $refreshtime = 5;

    if ( isset( $args[ 'name' ] ) ) {
      $name = $args[ 'name' ];
    } else {
      $name = null;
    }
    
    if ( isset( $args[ "email" ] ) ) {
      $email = $args[ "email" ];
    } else {
      $email = null;
    }

    if (($name == NULL) || ($email == NULL)) {
      echo "<html>\n";
      echo "  <head>\n";
      echo "    <meta http-equiv=\"REFRESH\" content=\"$refreshtime;url=index.php\">\n";
      echo "    <title>Forms - PHP App</title>\n";
      echo "  </head>\n";
      echo "  <body>\n";
      echo "    <p> Invalid data!";
      echo "    <p> You will be redirect to the login page in $refreshtime seconds\n";
      echo "  </body>\n";
      echo "</html>";
    } else {
      echo "<html>\n";
      echo "  <head>\n";
      echo "    <title>Forms - PHP App</title>\n";
      echo "  </head>\n";
      echo "  <body>\n";
      echo "    <p>Hello $name, your e-mail is $email\n<br>";
      echo "    <p><a href=\"formUpdateProfile.php\">Update profile</a>";
      echo "  </body>\n";
      echo "</html>";
    }
    ?>
  </body>
</html>
