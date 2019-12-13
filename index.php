<html lang="en">
    <head>
        <meta charset="utf-8"/>
        <title>AliBestOf</title>
        <meta name="description" content=""/>
        <meta name="keywords" content=""/>
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
        <meta name="author" content="Piotr Bartoszewski">
        <meta name="viewport" content="width=device-width"/>
        <!--<link rel="stylesheet" href="css/style.css" type="text/css">-->
        <link href="img/icons/icon.png" rel="shortcut icon">
        <link href="https://fonts.googleapis.com/css?family=Nunito|Open+Sans&display=swap" rel="stylesheet">


        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
        <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
        
        <script>
            window.ao_subid = "";
        </script>
        <script src="//js.mamydirect.com/js/?h=kJlyQUb9" type="text/javascript" async></script>

        <script>
            document.addEventListener('contextmenu', event => event.preventDefault());
        </script>
    </head>

    <body>
        <header class="container-sm">
            <a href="index.php" class="text-center" style="padding:1rem">
                <p class="h1">AliBestOf</p>
            </a>
        </header>

        <nav class="container-sm sticky-top">
            <form action="search.php" method="get">
                <div class="input-group mb-3">
                    <input type="text" name="query" class="form-control" placeholder="Search for products..." aria-label="Search for products...">
                    <button type="submit" class="btn btn-primary">&#x1F50D</button>
                </div>
            </form>
        </nav>

        <article class="text-center" style="margin-top: 2rem;">
            <?php
            $itemsPerPage = 40;

            if (isset($_GET["page"]) && !empty($_GET["page"]))
                $currentPage = $_GET["page"];
            else
                $currentPage = 1;

            $start = ($currentPage - 1) * $itemsPerPage;
            $limit = $itemsPerPage;

            require_once "dbConnect.php";

            if ($result = @$connection->query("SELECT * FROM $table_products WHERE hidden=0 ORDER BY id DESC LIMIT {$start}, {$limit} ")) {
                foreach ($result as $product) {
                    $imgPath = "img/products/{$product['name']}";

                    if(file_exists($imgPath.".png"))
                        $imgPath = $imgPath.".png";
                    else if(file_exists($imgPath.".jpg"))
                        $imgPath = $imgPath.".jpg";
                    else if(file_exists($imgPath.".jpeg"))
                        $imgPath = $imgPath.".jpeg";
                    else if(file_exists($imgPath.".gif"))
                        $imgPath = $imgPath.".gif";

                    echo <<< _END

    <form action="productInfo.php" method="GET" style="display:inline-block; width: 10rem;">
        <div class="card">
          <img src="{$imgPath}" style="width: 100%; height: 10rem; object-fit: cover; margin: 0 auto;" alt="{$product['name']}/>
          <div class="card-body">
            <input type="text" class="form-control" readonly="readonly" value="{$product['name']}"/>
            <input type="hidden" name="productName" value="{$product['name']}"/>
            <button type="submit" class="btn btn-primary">More</button>
          </div>
        </div>
    </form>

_END;
                }
            } else {
                echo "No such table '$table_products' found in the database";
                exit();
            }
            ?>
        </article>

        <nav>
            <ul class="pagination justify-content-center">
                <?php
                $totalItems = @$connection->query("SELECT * FROM $table_products WHERE hidden=0")->num_rows;
                $totalPages = ceil($totalItems / $itemsPerPage);

                if($totalPages > 1) {
                    echo '<br/><br/>';
                    for ($i = 1; $i <= $totalPages; $i++) {
                        echo <<< _END
                        <li class="page-item"><a class="page-link" href="index.php?page=$i">$i</a></li>
_END;
                    }
                }
                ?>
            </ul>
        </nav>

        <footer class="card">
            <div class="card-body">
                <h5 class="card-title text-center">&copy AliBestOf All Rights Reserved!</h5>
            </div>
        </footer>
    </body>
</html>