<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
    <title>Login form for a big screen - Forms App</title>
    
    <link REL="stylesheet" TYPE="text/css" href="../Styles/GlobalStyle.css">

    <script type="text/javascript" src="scripts/forms.js">
    </script>
  </head>

  <body>
    <table>
      <tr>
        <td>
          <img src="images/LogoBig.png" alt="Logo"/>
        </td>
        <td>
          <h1 align="center">Processing HTML forms with PHP</h1>    
        </td>
      </tr>    
    </table>

    <br>

    <form 
      action="processLogin.php"
      onsubmit="return FormLoginValidator(this)"
      name="FormLogin"
      method="post" >
      <table>
        <tr>
          <td>Name:</td>
          <td><input onclick="myFunc2()" type="text" name="name" value="Type your name"></td>
        </tr>
        <tr>
          <td>E-mail:</td>
          <td><input type="text" name="email" value="@isel.pt"></td>
        </tr>
        <tr>
          <td>
            <input type="submit" value="Send">
          </td>
          <td>
            <input type="reset" value="Reset">
          </td>
        </tr>        
      </table>
    </form>

    <p><b>Note:</b></p>
    <?php
      include_once( "../Lib/db.php" );

      $pathConfigFile = ConfigFile;

      echo "    <p>Data base settings are located at:</p>\n";
      echo "    <p>$pathConfigFile</p>\n";
      echo "    <p>Before run this example update your settings (host/port/database name/username/password).</p>\n<br>";

      echo "    <p>Please ensure that PHP extentions for mysql are enable:</p>\n<br>";

      echo "    <code>extension=php_mysqli.dll</code> in \"php.ini\" file +/- line 891\n<br>";
    ?>
  </body>
</html>
