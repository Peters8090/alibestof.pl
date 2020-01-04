<html lang="en">
<head>
    <meta charset="utf-8"/>
    <title>AliBestOf</title>
    <meta name="description" content=""/>
    <meta name="keywords" content=""/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
    <meta name="author" content="Piotr Bartoszewski">
    <meta name="viewport" content="width=device-width"/>
    <link rel="stylesheet" href="css/style.css" type="text/css">
    <link href="img/icons/icon.png" rel="shortcut icon">
    <link href="https://fonts.googleapis.com/css?family=Nunito|Open+Sans&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
            integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n"
            crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
            integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6"
            crossorigin="anonymous"></script>

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

<nav class="container-md sticky-top">
    <form action="index.php" method="get">
        <div class="input-group mb-3">
            <input type="text" name="query" class="form-control" placeholder="Search for products..."
                   aria-label="Search for products...">
            <button type="submit" class="btn btn-primary">&#x1F50D</button>
        </div>
    </form>
</nav>

<article class="text-center">
    <?php

    require_once "dbConnect.php";

    if (isset($_GET["page"]) && !empty($_GET["page"])) {
        $_GET['page'] = htmlentities($_GET['page'], ENT_QUOTES, "UTF-8");
        $_GET['page'] = mysqli_real_escape_string($connection, $_GET['page']);

        $currentPage = $_GET["page"];
    } else
        $currentPage = 1;

    $itemsPerPage = 50;
    $start = ($currentPage - 1) * $itemsPerPage;
    $limit = $itemsPerPage;

    if (isset($_GET["query"]) && !empty($_GET["query"])) {
        $_GET['query'] = htmlentities($_GET['query'], ENT_QUOTES, "UTF-8");
        $_GET['query'] = mysqli_real_escape_string($connection, $_GET['query']);
    }

    if ($result = @$connection->query(
        (
            isset($_GET["query"]) && !empty($_GET["query"])) ?
            "SELECT * FROM $table_products WHERE hidden=0 AND (id='{$_GET['query']}' OR (name LIKE '%{$_GET['query']}%')  OR (description LIKE '%{$_GET['query']}%')) ORDER BY id DESC" :
            "SELECT * FROM $table_products WHERE hidden=0 ORDER BY id DESC LIMIT {$start}, {$limit}"
    )) {
        if (($result->num_rows) == 0) {
            echo <<< _END
                    <br/>
                    <p class="h5">Not found</p>
_END;
            exit();
        }
        foreach ($result as $product) {
            $imgPath = "img/products/{$product['id']}";

            if (file_exists($imgPath . ".png"))
                $imgPath = $imgPath . ".png";
            else if (file_exists($imgPath . ".jpg"))
                $imgPath = $imgPath . ".jpg";
            else if (file_exists($imgPath . ".jpeg"))
                $imgPath = $imgPath . ".jpeg";
            else if (file_exists($imgPath . ".gif"))
                $imgPath = $imgPath . ".gif";

            echo <<< _END

    <form action="productInfo.php" method="GET" class="product">
        <div class="card">
          <img src="{$imgPath}" alt="{$product['id']}/>
          <div class="card-body">
            <input type="text" class="form-control" readonly="readonly" value="{$product['name']}"/>
            <input type="hidden" name="id" value="{$product['id']}"/>
            <button type="submit" class="btn btn-primary">More</button>
          </div>
        </div>
    </form>

_END;
        }
    } else {
        echo "<p class='h5>Error: $connection->connect_errno</p>";
        exit();
    }
    ?>
</article>

<nav>
    <ul class="pagination justify-content-center">
        <?php
        $totalItems = @$connection->query("SELECT * FROM $table_products WHERE hidden=0")->num_rows;
        $totalPages = ceil($totalItems / $itemsPerPage);

        if ($totalPages > 1 && (!isset($_GET["query"]) || empty($_GET["query"]))) {
            echo '<br/><br/>';
            if ($currentPage == 1) {
                echo <<< _END
                        <li class="page-item disabled">
                              <a class="page-link" href="#" aria-disabled="true"><</a>
                            </li>
_END;
            } else {
                $previous = $currentPage - 1;
                echo <<< _END
                        <li class="page-item">
      <a class="page-link" href="index.php?page=$previous"><</a>
    </li>
_END;
            }

            for ($i = 1; $i <= $totalPages; $i++) {
                if ($i == 1 || $i == $totalPages || $i == $currentPage || $i == $currentPage - 1 || $i == $currentPage + 1) {
                    if ($i == $totalPages) {
                        echo <<< _END
                        <form action="index.php">
                            <input type="number" placeholder="..." min="1" max="$totalPages" class="pagination-number-input" name="page" onKeyDown="if(this.value.length==2 && event.keyCode>47 && event.keyCode < 58)return false;">
                        </form>
_END;
                    }

                    if ($i == $currentPage) {
                        echo <<< _END
                        <li class="page-item active"><a class="page-link" href="#">$i</a></li>
_END;
                    } else {
                        echo <<< _END
                        <li class="page-item"><a class="page-link" href="index.php?page=$i">$i</a></li>
_END;
                    }
                }
            }

            if ($currentPage == $totalPages) {
                echo <<< _END
                        <li class="page-item disabled">
                              <a class="page-link" href="#" aria-disabled="true">></a>
                            </li>
_END;
            } else {
                $next = $currentPage + 1;
                echo <<< _END
                        <li class="page-item">
      <a class="page-link" href="index.php?page=$next">></a>
    </li>
_END;
            }
        }
        ?>
    </ul>
</nav>

<footer class="card">
    <div class="card-body">
        <h5 class="card-title text-center">&copy AliBestOf 2020 | All Rights Reserved!</h5>
    </div>
</footer>
</body>
</html>