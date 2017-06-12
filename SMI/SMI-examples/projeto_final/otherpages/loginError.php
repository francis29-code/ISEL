<?php

if($_POST){
  require_once("../lib/db.php");

  $username = $_POST['username'];
  $password = $_POST['password'];

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

  //faz verificação se o utilizador já validou o email
  if(mysqli_num_rows($result)==1 && ($password_md5 == $value_password)){
    session_start();
    $_SESSION['auth'] = 'true';
    //guardamos em sessão qual o tipo de utilizador a dar login
    $_SESSION['tipo'] = $value_tipo;

    switch($value_tipo){
      //não existe caso para o visitante pois esse apenas vizuliza a primeira pagina do MEO SUDOESTE
      case 'subscritor':
            //se o login se verificar direciona-o para a o seu feed, com algumas opções extra
            echo "<script>window.location.href = '../smi-rolo/PhpProject1/Feed.php'</script>";
      case 'normal':
            //se o login se verificar direciona-o para a o seu feed
            echo "<script>window.location.href = '../index.php'</script>";
      case 'admin':
            //se o login se verificar direciona-o para a página de admin
            echo "<script>window.location.href = '../smi-rolo/PhpProject1/indexAdmin.php'</script>";
    }
  }else{
    echo"<script>window.location.href = 'loginError.php'</script>";
  }
  dbDisconnect();
}

?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Login</title>
  <!-- Tell the browser to be responsive to screen width -->
  <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
  <!-- Bootstrap 3.3.6 -->
  <link rel="stylesheet" href="../assets/bootstrap/css/bootstrap.min.css">
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css">
  <!-- Ionicons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.min.css">
  <!-- Theme style -->
  <link rel="stylesheet" href="../assets/dist/css/AdminLTE.min.css">
  <!-- iCheck -->
  <link rel="stylesheet" href="../assets/plugins/iCheck/square/blue.css">

  <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
  <![endif]-->
</head>
<body class="hold-transition login-page">
<div class="login-box">
  <div class="login-logo">
    <a href="../index.php"><b>MEO</b>Sudoeste</a>
  </div>
  <!-- /.login-logo -->
  <div class="login-box-body">
    <p class="login-box-msg">Sign in to start your session</p>

    <form method="POST">
      <div class="form-group has-feedback">
        <input type="text" class="form-control" placeholder="Username" name="username">
        <span class="glyphicon glyphicon-user form-control-feedback"></span>
      </div>
      <div class="form-group has-error">
        <input type="password" class="form-control" placeholder="Password" name="password">
        <span class="glyphicon glyphicon-lock form-control-feedback"></span>
        <span class='help-block'>Wrong Password</span>
      </div>
      <div class="row">
        <!-- /.col -->
        <div class="col-xs-12">
          <input type="submit" class="btn btn-primary btn-block btn-flat"></input>
        </div>
        <!-- /.col -->
      </div>
    </form>
    <!-- /.social-auth-links -->

    <a href="#">I forgot my password</a><br>
    <a href="registo.php" class="text-center">Register a new membership</a>

  </div>
  <!-- /.login-box-body -->
</div>
<!-- /.login-box -->

<!-- jQuery 2.2.3 -->
<script src="../assets/plugins/jQuery/jquery-2.2.3.min.js"></script>
<!-- Bootstrap 3.3.6 -->
<script src="../assets/bootstrap/js/bootstrap.min.js"></script>
<!-- iCheck -->
<script src="../assets/plugins/iCheck/icheck.min.js"></script>
<script>

  $(function () {
    $('input').iCheck({
      checkboxClass: 'icheckbox_square-blue',
      radioClass: 'iradio_square-blue',
      increaseArea: '100%' // optional
    });
  });
</script>
</body>
</html>
