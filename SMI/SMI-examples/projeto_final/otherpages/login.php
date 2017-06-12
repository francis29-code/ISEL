
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

    <form method="POST" onsubmit="return validateForm()">
      <div class="form-group has-feedback">
        <input type="text" class="form-control" placeholder="Username" name="username">
        <span class="glyphicon glyphicon-user form-control-feedback"></span>
      </div>
      <div class='form-group has-feedback' id="password">
        <input type='password' class='form-control' placeholder='Password' name='password'>
        <span class='glyphicon glyphicon-lock form-control-feedback'></span>
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
  function validateForm(){
    var xhttp = new XMLHttpRequest();
    var currentPassword = $("input[name='password']").val();
    var currentUser = $("input[name='username']").val();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        switch(xhttp.responseText){
          case 'normal':
            window.location.href = "../index.php";
            break;
          case 'subscritor':
            window.location.href = "../index.php";
            break;
          case 'admin':
            window.location.href = "../indexAdmin.php";
            break;
          default:
            $("#label").remove();
            $("#labelhelper").remove();
            $("#password").attr('class','form-group has-error');
            $("#password").prepend("<label class='control-label' for='inputError' id='label'><i class='fa fa-times-circle-o'></i>Input with error</label>");
            $("#password").append("<span class='help-block' id='labelhelper'>Credenciais Invalidas</span>");
        }
      }
    };
    xhttp.open('POST', "auxPages/auxLoginPassword.php?currentPassword="+currentPassword+"&currentUsername="+currentUser, true);
    xhttp.send();

    //impede o form de dar submit e de dar reload à pagina
    return false;
  }

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
