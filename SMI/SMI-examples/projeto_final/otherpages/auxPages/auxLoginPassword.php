<?php
//session start sempre que quiser fazer alterações ou aceder a variaveis
session_start();
require_once("../../lib/db.php");

$username = $_GET['currentUsername'];
$password = $_GET['currentPassword'];

dbConnect(credenciaisDB);

mysqli_select_db($GLOBALS['ligacao'], $GLOBALS['configDataBase']->db);

//comparação da password em MD5
$password_md5 = md5($password);

$query = "SELECT * FROM `userclient` WHERE username='$username'";

$result = mysqli_query($GLOBALS['ligacao'], $query);
$result_array = mysqli_fetch_array($result);
$value_tipo = $result_array['tipo'];
$value_valido = $result_array['valido'];
$value_password = $result_array['password'];

dbDisconnect();

//faz verificação se o utilizador já validou o email
if(mysqli_num_rows($result)==1 && ($password_md5 == $value_password) && $value_valido == "1"){
  //para efeitos do Feed
  $_SESSION['username'] = $username;
  //guardamos em sessão qual o tipo de utilizador a dar login
  $_SESSION['tipo'] = $value_tipo;

  echo"$value_tipo";
}else{
  echo"invalido";
}

?>
