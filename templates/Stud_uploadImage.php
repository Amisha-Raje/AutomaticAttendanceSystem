<html lang="en">
<head>
    <title>Image Upload</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="navbar.css">
    <link rel="stylesheet" href="view.css">
</head>
<body>
<!--Navigation bar-->
<nav class="navbar navbar-default navbar-fixed-top" style="background-color:#191970;">
                <div class="container">
                <div class="navbar-header">

                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
        
                    <div class="col-md-3 col-sm-6 col-xs-12 left" id ="left">  
                        <img src="col_logo.png" width="100px" height="100px" id=logo alt="Logo image" style="margin-left: -30%;" />
                    </div>
                    <a class="navbar-brand" href="homepage.php" style="color:white;font-size:155%;"><span> Automatic Attendance System</span></a>
                    <br>
                </div>
                <div class="collapse navbar-collapse" id="myNavbar" >
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="homepage.php" class="dropdown" style="color:#f5f5f5;">Home</a></li>  
                    </ul>
                </div>
                </div>
                </nav>
        <!--/ Navigation bar-->

        <!-- Banner-->
                <div class="banner">
                <div class="bg-color">
                <div class="container">
                    <div class="row">
                        <div class="banner-text text-center">
                            <div class="text-border">
                                <h2 class="text-dec">Learn To Code</h2>
                            </div>
                            <div class="intro-para text-center quote">
                                <p><br><br></p>
                            </div>
                            <a href="#feature" class="mouse-hover">
                                <div class="mouse"></div>
                            </a>
                        </div>
                    </div>
                </div>
                </div>
                </div>
        <!--/ Banner-->
<div class="box">
    <!-- <h1 style="margin-top:100px;">Welcome, <?php echo $_SESSION["username"] ?>! </h1> -->
<!-- </div>

<div class="upload-form"> -->
    <form action="Stud_uploadImage.php" method="post" enctype="multipart/form-data">
        <label for="image"><h1>Select Image</h1></label>
        <input type="file" name="image" id="image">
        <input type="submit" value="Upload Image" class="button" name="submit">
    </form>
</div>

</body>
</html>
