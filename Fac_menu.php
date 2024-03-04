<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Welcome</title>
        <meta charset="UTF-8">
	    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
	    <link rel="stylesheet" href="View.css">
        <link rel="stylesheet" href="navbar.css">
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
			<!-- <h1>Welcome! </h1> -->
		    <input class="button" type="submit" name="e" value="Add Course" onClick="document.location.href='Fac_addCourse.php'" >
		    <input class="button" type="submit" name="e" value="Take Attendance" onClick="document.location.href='Fac_takeAtt.php'" >
		    <input class="button" type="submit" name="e" value="Show Attendance" onClick="document.location.href='Alu_update.php'" >
		    <input class="button" type="submit" name="l" value="Logout" onClick="document.location.href='Alu_logout.php'"  >
        </div>
    </body>
</html>