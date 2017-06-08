<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
    <title>Login form for a small screen - Forms App</title>
    
    <link REL="stylesheet" TYPE="text/css" href="../Styles/GlobalStyle.css">
  </head>

  <body>
    <table>
      <tr>
        <td>
          <img src="images/LogoSmall.png" alt="Logo"/>
        </td>
        <td>
          <h3 align="center">Processing HTML forms with PHP</h3>
        </td>
      </tr>    
    </table>

    <br>

    <form action="processLogin.php" method="post" >
      <table>
        <tr>
          <td>Name:</td>
        </tr>
        <tr>
          <td><input type="text" name="name" value="Type your name"></td>
        </tr>
        <tr>
          <td>E-mail:</td>
        </tr>
        <tr>
          <td><input type="text" name="email" value="@isel.pt"></td>
        </tr>
      </table>

      <input type="submit" value="Send">
      <input type="reset" value="Reset">
    </form>
  </body>
</html>
