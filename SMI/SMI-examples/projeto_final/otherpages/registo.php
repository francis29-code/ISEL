<?php
if($_POST){
  require_once("../lib/db.php");
  //variaveis para a cricao de um registo
  $tipo = $_POST['tipo'];
  $nome = $_POST['nome'];
  $username = $_POST['username'];
  $password = md5($_POST['password']);
  $email = $_POST['email'];
  $valido =  $_POST['valido'];
  // fotografia logo no registo?---------------------------
  $fotografia =  $_POST['fotografia'];

  dbConnect(credenciaisDB);

  mysqli_select_db($GLOBALS['ligacao'], $GLOBALS['configDataBase']->db);

  $query = "INSERT INTO `userclient` VALUES ('$tipo', '$nome', '$username',
    '$password', '$email', '$valido', '$fotografia')";

  $result = mysqli_query($GLOBALS['ligacao'],$query);

  dbDisconnect();
}
 ?>

 <!DOCTYPE html>
 <html>
 <head>
   <meta charset="utf-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <title>Registration Page</title>
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
 <body class="hold-transition register-page">
 <div class="register-box">
   <div class="register-logo">
     <a href="../index.php"><b>MEO</b>Sudoeste</a>
   </div>

   <div class="register-box-body">
     <p class="login-box-msg">Register a new membership</p>
     <!-- teste - index.php depois modificar -->
     <form method="post" action="../index.php">
       <!-- quando o utilizador se regista e sempre uma subscrição normal, se desejar
       outro tipo de subscrição recorre a pagamentos -->
       <div class="form-group has-feedback">
         <input type="hidden" value="normal" name="tipo">
       </div>
       <div class="form-group has-feedback">
         <input type="hidden" value="0" name="valido">
       </div>
       <div class="form-group has-feedback">
         <input type="hidden" value="cenas" name="fotografia">
       </div>
       <div class="form-group has-feedback">
         <input type="text" class="form-control" placeholder="First and Last name" name="nome">
         <span class="glyphicon glyphicon-user form-control-feedback"></span>
       </div>
       <div class="form-group has-feedback" id="username">
         <input type="text" class="form-control" placeholder="Username" name="username" onchange="checkUsername()">
         <span class="glyphicon glyphicon-user form-control-feedback"></span>
       </div>
       <div class="form-group has-feedback">
         <input type="email" class="form-control" placeholder="Email" name="email">
         <span class="glyphicon glyphicon-envelope form-control-feedback"></span>
       </div>
       <div class="form-group has-feedback">
         <input type="password" class="form-control" placeholder="Password" name="password" onchange="checkPassword()">
         <span class="glyphicon glyphicon-lock form-control-feedback"></span>
       </div>
       <div class="form-group has-feedback" id="re_password">
         <input type="password" class="form-control" placeholder="Retype password" name="re_password" onchange="checkPassword()">
         <span class="glyphicon glyphicon-log-in form-control-feedback"></span>
       </div>
       <div class="form-group">
         <label for="exampleInputFile">File input</label>
         <input type="file" id="exampleInputFile">
         <p class="help-block">Example block-level help text here.</p>
       </div>
       <div class="row">
         <div class="col-xs-8">
           <div class="checkbox icheck">
             <label>
               <input type="checkbox"> I agree to the <a href="#">terms</a>
             </label>
           </div>
         </div>
         <!-- /.col -->
         <div class="col-xs-4">
           <button type="submit" class="btn btn-primary btn-block btn-flat" data-toggle="modal" data-target=".modal">Registar</button>
         </div>
         <!-- /.col -->
       </div>
     </form>
     <div class="example-modal">
      <div class="modal modal-warning">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span></button>
              <h4 class="modal-title">Email Confirmation</h4>
            </div>
            <div class="modal-body">
              <p>An e-mail with a confirmation lik has been sent, please check your e-mail.&hellip;</p>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-outline pull-left" data-dismiss="modal">Close</button>
            </div>
          </div>
          <!-- /.modal-content -->
        </div>
        <!-- /.modal-dialog -->
      </div>
      <!-- /.modal -->
    </div>
    <!-- /.example-modal -->

     <a href="login.php" class="text-center">I already have a membership</a>
   </div>
   <!-- /.form-box -->
 </div>
 <!-- /.register-box -->

 <!-- jQuery 2.2.3 -->
 <script src="../assets/plugins/jQuery/jquery-2.2.3.min.js"></script>
 <!-- Bootstrap 3.3.6 -->
 <script src="../assets/bootstrap/js/bootstrap.min.js"></script>
 <!-- iCheck -->
 <script src="../assets/plugins/iCheck/icheck.min.js"></script>
 <script>
  function checkUsername(){
      var xhttp = new XMLHttpRequest();
      var currentUser = $("input[name='username']").val();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          switch(xhttp.responseText){
            case 'true':
              //username available
              $("#labelUser").remove();
              $("#labelhelperUser").remove();
              $("#username").attr('class','form-group has-success');
              $("#username").prepend("<label class='control-label' for='inputSuccess' id='labelUser'><i class='fa fa-check'></i>Input with success</label>");
              $("#username").append("<span class='help-block' id='labelhelperUser'>Username Available</span>");
              break;
            case 'false':
              $("#labelUser").remove();
              $("#labelhelperUser").remove();
              $("#username").attr('class','form-group has-error');
              $("#username").prepend("<label class='control-label' for='inputError' id='labelUser'><i class='fa fa-times-circle-o'></i>Input with error</label>");
              $("#username").append("<span class='help-block' id='labelhelperUser'>Username Unavailable</span>");
              break;
          }
        }
      };
      xhttp.open('GET', "auxPages/auxNameChecker.php?currentUsername="+currentUser, true);
      xhttp.send();

  }

  function checkPassword(){
     //verificar se as duas passwords estão iguais
    //  global equal = false;
     var re_password = $("input[name='re_password']").val();
     var password = $("input[name='password']").val();
     if(re_password == ""){
       $("#label").remove();
       $("#labelhelper").remove();
       $("#re_password").attr('class','form-group has-default');
     }else{
       if(re_password == password){
         $("#label").remove();
         $("#labelhelper").remove();
         $("#re_password").attr('class','form-group has-success');
         $("#re_password").prepend("<label class='control-label' for='inputSuccess' id='label'><i class='fa fa-check'></i>Input with success</label>");
         $("#re_password").append("<span class='help-block' id='labelhelper'>Matching passwords</span>");
       }else{
         $("#label").remove();
         $("#labelhelper").remove();
         $("#re_password").attr('class','form-group has-error');
         $("#re_password").prepend("<label class='control-label' for='inputError' id='label'><i class='fa fa-times-circle-o'></i>Input with error</label>");
         $("#re_password").append("<span class='help-block' id='labelhelper'>Different passwords</span>");
       }
     }
   }

   $(function () {
     $('input').iCheck({
       checkboxClass: 'icheckbox_square-blue',
       radioClass: 'iradio_square-blue',
       increaseArea: '20%' // optional
     });
   });
 </script>
 </body>
 </html>
