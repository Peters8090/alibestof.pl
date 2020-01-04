<?php
if (!isset($_GET['id']) || empty($_GET['id'])) {
    header('Location: index.php');
}
require_once "dbConnect.php";
$_GET['id'] = htmlentities($_GET['id'], ENT_QUOTES, "UTF-8");
$_GET['id'] = mysqli_real_escape_string($connection, $_GET['id']);
$sql = "SELECT * FROM $table_products WHERE hidden=0 AND id='{$_GET['id']}'";
if ($result = $connection->query($sql)) {
    if (($result->num_rows) == 0) {
        header("Location: index.php");
    }
}
?>

<html lang="en">
    <head>
        <meta charset="utf-8"/>
        <title>AliBestOf - Product <?php echo"{$_GET['id']}"?></title>
        <meta name="description" content=""/>
        <meta name="keywords" content=""/>
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
        <meta name="author" content="Piotr Bartoszewski">
        <meta name="viewport" content="width=device-width"/>
        <link rel="stylesheet" href="css/style.css" type="text/css">
        <link href="img/icons/icon.png" rel="shortcut icon">
        <link href="https://fonts.googleapis.com/css?family=Nunito|Open+Sans&display=swap" rel="stylesheet">

        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

        <script>
            window.ao_subid = "";
        </script>
        <script src="//js.mamydirect.com/js/?h=kJlyQUb9" type="text/javascript" async></script>

        <script>
            document.addEventListener('contextmenu', event => event.preventDefault());
        </script>
    </head>

    <body>
        <header>
            <a href="index.php" class="title">
                <img src="img/icons/icon.png"/>
                <p class="h1">liBestOf</p>
            </a>
        </header>

        <article class="text-center">
            <?php
    if ($result = $connection->query($sql)) {
        $product = $result->fetch_assoc();
        $imgPath = "img/products/{$product['id']}";

        if(file_exists($imgPath.".png"))
            $imgPath = $imgPath.".png";
        else if(file_exists($imgPath.".jpg"))
            $imgPath = $imgPath.".jpg";
        else if(file_exists($imgPath.".jpeg"))
            $imgPath = $imgPath.".jpeg";
        else if(file_exists($imgPath.".gif"))
            $imgPath = $imgPath.".gif";
        echo <<< _END
        <div>
            <div class="card mb-3" >
              <div class="row no-gutters">
                <div class="col-md-4">
                  <img src="{$imgPath}" class="card-img w-50 img-thumbnail" alt="{$product['name']}">
                </div>
                <div class="col-md-8">
                  <div class="card card-body justify-content-center" id="productInfo-card-body">
                    <h5 class="card-title">{$product['name']}</h5>
                    <p class="card-text">{$product['description']}</p>
                    <form action="{$product['reflink']}">
                        <button type="submit" class="btn btn-primary">Link</button>
                    </form>
                  </div>
                </div>
              </div>
            </div>
        </div>

        <iframe src="{$product['link']}" align="center" width="100%" height="50%" frameborder="0"></iframe>
_END;
    } else {
        echo <<< _END
    <p class="h5">Error: $connection->connect_errno</p>
_END;
        exit();
    }
            ?>
        </article>
        <footer class="card">
            <div class="card-body">
                <h5 class="card-title text-center">&copy AliBestOf 2020 | All Rights Reserved!</h5>
            </div>
        </footer>
    </body>
</html>