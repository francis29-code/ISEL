<!DOCTYPE html>
<?php
//fazemos session start apenas uma vez
session_start();

if(!isset($_SESSION['tipo']) && empty($_SESSION['tipo'])){
  $_SESSION['tipo'] = 'visitante';
}

?>

<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>MEO Sudoeste</title>
  <!-- Tell the browser to be responsive to screen width -->
  <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
  <!-- Bootstrap 3.3.6 -->
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css">
  <!-- Ionicons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.min.css">
  <!-- Theme style -->
  <link rel="stylesheet" href="assets/dist/css/AdminLTE.min.css">
  <!-- AdminLTE Skins. Choose a skin from the css/skins
       folder instead of downloading all of them to reduce the load. -->
  <link rel="stylesheet" href="assets/dist/css/skins/_all-skins.min.css">

  <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
  <![endif]-->
</head>
<!-- ADD THE CLASS layout-top-nav TO REMOVE THE SIDEBAR. -->
<body class="hold-transition skin-blue layout-top-nav">
<div class="wrapper">

  <header class="main-header">
    <nav class="navbar navbar-static-top">
      <div class="container">
        <div class="navbar-header">
          <a href="#" onclick="tipo()" class="navbar-brand"><b>MEO</b>Sudoeste</a>
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-collapse">
            <i class="fa fa-bars"></i>
          </button>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse pull-left" id="navbar-collapse">
          <ul class="nav navbar-nav">
            <li><a href="otherpages/login.php">Login</a></li>
            <li><a href="otherpages/registo.php">Register</a></li>
            <!-- <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <span class="caret"></span></a>
              <ul class="dropdown-menu" role="menu">
                <li><a href="#">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>
                <li class="divider"></li>
                <li><a href="#">Separated link</a></li>
                <li class="divider"></li>
                <li><a href="#">One more separated link</a></li>
              </ul>
            </li> -->
          </ul>
        </div>
        <!-- /.navbar-collapse -->
      </div>
      <!-- /.container-fluid -->
    </nav>
  </header>
  <!-- Full Width Column -->
  <div class="content-wrapper">
    <div class="container">
      <!-- Content Header (Page header) -->
      <section class="content-header">
      </section>

      <!-- Main content -->
      <section class="content">

        <div class="row">
          <div class="col-md-14">
            <div class="box box-primary">
            <div class="slideshow-container">

              <div class="mySlides fade">
                <div class="numbertext">1 / 4</div>
                <img src="assets/slideshow/img/sw3.jpg" style="width:100%">
              </div>

              <div class="mySlides fade">
                <div class="numbertext">2 / 4</div>
                <img src="assets/slideshow/img/sw2.jpg" style="width:100%">
              </div>

              <div class="mySlides fade">
                <div class="numbertext">3 / 4</div>
                <img src="assets/slideshow/img/sw4.jpg" style="width:100%">
              </div>
              <div class="mySlides fade">
                <div class="numbertext">4 / 4</div>
                <img src="assets/slideshow/img/sw1.jpg" style="width:100%">
              </div>
              <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
              <a class="next" onclick="plusSlides(1)">&#10095;</a>
            </div>
            <br>

            <div style="text-align:center">
              <span class="dot" onclick="currentSlide(1)"></span>
              <span class="dot" onclick="currentSlide(2)"></span>
              <span class="dot" onclick="currentSlide(3)"></span>
              <span class="dot" onclick="currentSlide(4)"></span>
            </div>

            <div class="box-body">

              <h3 class="box-title" style="text-align:center;margin-top:5%;">Quem somos</h3>
              <div class="box-body">Bacon ipsum dolor amet brisket turducken picanha, burgdoggen cow doner t-bone cupim sausage pig tri-tip swine alcatra tail. Ham hock sirloin pork chop bresaola t-bone chuck. Ham ground round chicken sausage jowl, shank jerky kielbasa strip steak ham hock venison pig corned beef pastrami. Shank swine pork shoulder pig. Salami bacon porchetta chicken drumstick, turducken cow fatback flank shank.
                <br>
                <br>
                Burgdoggen tongue porchetta brisket capicola corned beef swine ribeye ground round beef ribs short ribs andouille pork belly. Pork belly bacon venison andouille chicken. Burgdoggen capicola shank short loin corned beef alcatra strip steak ham bresaola pastrami sausage. Short ribs frankfurter short loin doner ground round. Brisket shank biltong tongue turducken porchetta alcatra shankle. Rump sirloin picanha filet mignon bresaola, fatback jowl pig swine shankle pork belly burgdoggen ground round. Fatback venison picanha, shoulder chicken chuck sausage jerky.
                <br>
                <br>
                Shoulder brisket frankfurter cow ham hock tongue pork belly ribeye shank tri-tip tenderloin kevin rump boudin. Biltong beef turkey frankfurter. Cupim ball tip pork belly drumstick turkey strip steak. Frankfurter venison fatback, bresaola tenderloin chicken tri-tip short loin burgdoggen jerky capicola rump. Sausage tenderloin tri-tip burgdoggen bacon kielbasa salami ball tip pancetta spare ribs cupim jerky. Filet mignon brisket shankle, chicken ground round ribeye kevin. Cow spare ribs biltong pork pancetta cupim frankfurter.
                <br>
                <br>
                Salami jowl tail, pork ribeye doner meatloaf swine picanha. Shoulder tri-tip pork belly bacon alcatra fatback. Cow burgdoggen venison, sirloin short loin turducken capicola frankfurter pork chop alcatra. T-bone capicola prosciutto swine meatloaf pork chop fatback. Corned beef beef ribs tail, spare ribs cow pork loin bacon meatloaf boudin ham.
                <br>
                <br>
                Pig beef landjaeger ground round kielbasa ham doner bacon pastrami jerky. Capicola salami sirloin prosciutto brisket, drumstick landjaeger spare ribs porchetta tongue kielbasa jerky biltong ham rump. Burgdoggen short loin beef ribs, ball tip tail ham hock meatball bacon corned beef pastrami. Ball tip turkey sausage hamburger ham hock kevin tongue salami filet mignon chicken porchetta. Andouille meatloaf turkey, pork loin beef alcatra bresaola hamburger.</div>
            </div>

          </div>

        </div>
        </div>

      </div>
      <!-- /.box -->
    </section>
      <!-- /.content -->
    </div>
    <!-- /.container -->
  </div>
  <!-- /.content-wrapper -->
  <footer class="main-footer">
    <div class="container">

      <strong>Copyright &copy; 2016-2017 <a>SMI -Fabio Rolo - Rui Santos</a>.</strong> All rights reserved.
    </div>
    <!-- /.container -->
  </footer>
</div>
<!-- ./wrapper -->

<!-- jQuery 2.2.3 -->
<script src="assets/plugins/jQuery/jquery-2.2.3.min.js"></script>
<!-- Bootstrap 3.3.6 -->
<script src="assets/bootstrap/js/bootstrap.min.js"></script>
<!-- SlimScroll -->
<script src="assets/plugins/slimScroll/jquery.slimscroll.min.js"></script>
<!-- FastClick -->
<script src="assets/plugins/fastclick/fastclick.js"></script>
<!-- AdminLTE App -->
<script src="assets/dist/js/app.min.js"></script>
<!-- AdminLTE for demo purposes -->
<script src="assets/dist/js/demo.js"></script>
<script>

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
</script>
<style>
* {box-sizing:border-box}
body {font-family: Verdana,sans-serif;margin:0}
.mySlides {display:none}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
  margin-top:5%;
}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  padding: 16px;
  margin-top: -22px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.8);
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  cursor:pointer;
  height: 13px;
  width: 13px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 4s;
  animation-name: fade;
  animation: fade 2s 1 forwards;
  animation-duration: 4s;
}

@-webkit-keyframes fade {
  from {opacity: 0.4}
  to {opacity: 1}
}

@KEYFRAMES FADE {
  FROM {OPACITY: .4}
  TO {OPACITY: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .prev, .next,.text {font-size: 11px}
}
</style>
</body>
</html>
