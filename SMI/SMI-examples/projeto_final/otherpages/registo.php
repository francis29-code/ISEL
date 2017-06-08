<?php
if($_POST){
  require_once("../lib/db.php");
  //variaveis para a cricao de um registo
  $tipo = $_POST['tipo'];
  $nome = $_POST['nome'];
  $username = $_POST['username'];
  $password = md5($_POST['password']);
  $email = $_POST['email'];
  $cc = $_POST['cc'];
  $valido =  $_POST['valido'];
  $fotografia =  $_POST['fotografia'];

  dbConnect(credenciaisDB);

  mysqli_select_db($GLOBALS['ligacao'], $GLOBALS['configDataBase']->db);

  $query = "INSERT INTO `userclient` VALUES ('$tipo', '$nome', '$username',
    '$password', '$email', '$cc', '$valido', '$fotografia')";

  $result = mysqli_query($GLOBALS['ligacao'],$query);

  if($result){
    header("location:login.php");
  }else{
    echo "wrong credencials";
  }
  dbDisconnect();
}
 ?>

<h1>Registo</h1>
<form class="form-horizontal" method="POST">
  <br>tipo:<input type="text" name="tipo"/><br>
  <br>nome completo:<input type="text" name="nome"/><br>
  <br>username:<input type="text" name="username"/><br>
  <br>password:<input type="password" name="password"/><br>
  <br>email:<input type="text" name="email"/><br>
  <br>cartao cidadao:<input type="text" name="cc"/><br>
  <input type="hidden" name="valido" value="1"/>
  <input type="hidden" name="fotografia" value="NULL"/>
  <br><input type="submit" value="Regista"/><br>
</form>
