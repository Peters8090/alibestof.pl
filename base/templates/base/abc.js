var ao_cpc_visit_ts = 0;
var ao_isSL = true;
if (typeof (ao_isST) == 'undefined' || ao_isST == null) var ao_isST = false;
var ao_isLB = true;
var ao_isNF = false;
var ao_st_marker = false;
var ao_sl_marker_active = false;
var ao_sl_marker = false;
var ao_sl_marker_tld_list = new Array();
var ao_sl_marker_info_class = false;
var ao_sl_marker_ignore_class = false;
var ao_sl_ignore_class = false;
var ao_sl_marker_class = 'ao_is_aff';
var ao_unlinklist = '';
if (typeof (ao_query) == 'undefined' || ao_query == null) var ao_query = '';
if (typeof (ao_subid) == 'undefined' || ao_subid == null) var ao_subid = '';
var ao_ex_el = 'html,head,style,script,img,iframe,select,input,textarea,title,link,audio,br,button,meta,a,object,iframe,ins,noscript,';
var ao_blacklist = "";
var ao_whitelist = "";
var ao_stw = [];
var ao_isIE = navigator.appName.indexOf("Explorer") != -1 ? true : false;
var ao_gf = false, ao_gg = 0, AO_MARKER_CHECK_RESULT = [];
var ao_gi = false;
var ao_aB = new Array("adgoal.de", "adtago.de", "addthis.com", "doubleclick.net", "doubleclick.net", "googleadservices.com", "googlesyndication.com", "google-analytics.com", "oingo.com", "urchin.com", "appliedsemantics.com", "overture.com", "intellitxt.com", "ligatus.com", "motorpresse.de", "freenet.de", "msn.com", "belboon.de", "adtech.de", "zanox.de", "zanox.com", "zanox-affiliate.de", "google.com", "google.at", "google.de", "comissionjunction.com", "cj.com", "qksrv.net", "dpbolvw.net", "adbutler.de", "tradedoubler.com", "quality-channel.de", "adition.com", "ligatus.de", "adpublisher.com", "webgains.de", "affiliwelt.net", "affiliwelt.de", "contaxe.com", "ad-srv.net", "adyard.de", "adverserve.net", "mediaplex.com", "smartadserver.com", "adalizer.com", "quartermedia.de", "mpnrs.com", "bluelithium.com", "adcloud.net", "performance-netzwerk.de", "erange.de", "twenga.de", "twenga.com", "clixgalore.com", "tradetracker.net", "shareasale.com", "pepperjamnetwork.com", "linksynergy.com", "retailerweb.net", "plista.com", "digidip.de", "digidip.net", "yieldkit.com", "facebook.com", "twitter.com", "adf.ly", "youtube.com", "imgbox.com", "yahoo.com", "outbrain.com", "wikipedia.org", "go2cloud.org", "whatsapp.com", "imagebam.com", "feedburner.com", "youtu.be", "instagram.com", "pinterest.com", "imgur.com", "spiegel.de", "bild.de", "reddit.com", "outbrain.com", "goo.gl", "bit.ly", "ktxtr.com", "admitad.com", "yandex.ru", "superclix.de", "webmasterplan.com", "whatsbroadcast.com");
var ao_aBU = ao_blacklist.split(",");
for (var x = 0; x < ao_aBU.length; x++) if (ao_aBU[x].length > 0) ao_aB.push(ao_aBU[x]);
var ao_uL = new Array();
if (ao_unlinklist != "") {
    var ao_uLU = ao_unlinklist.split(",");
    for (var x = 0; x < ao_uLU.length; x++) {
        ao_uL.push(ao_uLU[x]);
    }
}
var ao_aW = ao_whitelist.split(",");
for (var x = 0; x < ao_aW.length; x++) {
    if (ao_aW[x].length == 0) {
        ao_aW.splice(x, 1);
        x--;
    }
}
var ao_abpc = true;
var ao_gb = 4;

function ao_gc() {
    var ao_abt = document.createElement('script');
    ao_abt.src = '//abp.smartadcheck.de/js/abpc.js?#ads/banner/ad/';
    ao_abt.type = 'text/javascript';
    if (document.body) document.body.appendChild(ao_abt); else if (ao_gb > 0) {
        ao_gb--;
        setTimeout("ao_gc()", 200);
    }
}

ao_gc();

function ao_fc() {
    ao_isSL = false;
    if (typeof (ao_sl_sec) == "undefined" || ao_sl_sec == null || ao_sl_sec == "") {
        ao_fd(document.body);
    } else {
        var chk = false;
        for (var u = 0; u < ao_sl_sec.length; u++) {
            if (ao_sl_sec[u].n == 1) continue;
            var x = document.getElementsByTagName(ao_sl_sec[u].e);
            for (i = 0; i < x.length; i++) {
                if (ao_sl_sec[u].a == "class" && typeof (x[i].className.toLowerCase) == 'function') {
                    if (x[i].className.toLowerCase().substr(0, ao_sl_sec[u].v.length) == ao_sl_sec[u].v.toLowerCase()) {
                        ao_fd(x[i]);
                    }
                    chk = true;
                } else {
                    if (typeof (x[i].id.toLowerCase) == 'function') {
                        if (x[i].id.toLowerCase().substr(0, ao_sl_sec[u].v.length) == ao_sl_sec[u].v.toLowerCase()) {
                            ao_fd(x[i]);
                        }
                        chk = true;
                    }
                }
            }
        }
        if (!chk) {
            ao_fd(document.body);
        }
    }
    if (ao_sl_marker_active && !ao_gf && ao_sl_marker_tld_list.length > 0 && ao_gg == ao_sl_marker_tld_list.length && (!ao_isLB || ao_gi)) {
        ao_gf = true;
        ao_ge(JSON.stringify(ao_sl_marker_tld_list));
    } else {
        ao_gg = ao_sl_marker_tld_list.length;
    }
}

function ao_fd(sN) {
    if (sN != "undefined" && sN.childNodes != "undefined" && !ao_fk(sN, 0)) {
        var chN = sN.childNodes;
        var i = 0;
        while ((i < chN.length) && (chN.length != 0)) {
            if (chN[i] == "undefined") continue;
            var cN = chN[i];
            i++;
            if (cN.nodeType != 1) continue;
            if (cN.childNodes != "undefined" && cN.childNodes.length > 0 && ao_ex_el.indexOf(cN.nodeName.toLowerCase() + ',') === -1 && !ao_fk(cN, 0)) ao_fd(cN);
            if (cN.nodeName.toLowerCase() != "a") continue;
            if (cN.hasAttribute("ao_sl_mid")) continue;
            if (!ao_fk(cN, 0)) {
                ao_fe(cN);
            }
        }
    }
}

function ao_fe(cN) {
    if (cN.nodeName.toLowerCase() != "a") return;
    if (cN.href.substring(0, 4).toLowerCase() != "http") return;
    if (cN.href.substring(cN.href.length - 4).toLowerCase() in {
        '.jpg': '',
        '.bmp': '',
        '.pdf': '',
        '.png': '',
        '.zip': '',
        '.gif': ''
    }) return;
    var _x = cN.getAttribute("ao_sl_href", 0);
    if (_x && _x.length > 0) return;
    var locHost = location.hostname.replace("www.", "");
    if (locHost.indexOf(cN.hostname) != -1 || cN.hostname.indexOf(locHost) != -1) return;
    if (ao_sl_marker_ignore_class && cN.className && cN.className.indexOf(ao_sl_marker_ignore_class) != -1) {
        return;
    }
    for (var x = 0; x < ao_aB.length; x++) if (cN.hostname.indexOf(ao_aB[x]) != -1) return;
    if (ao_aW.length > 0) {
        var ao_gj = false;
        for (var x = 0; x < ao_aW.length; x++) {
            if (cN.hostname.indexOf(ao_aW[x]) != -1) {
                ao_gj = true;
                break;
            }
        }
        if (!ao_gj) {
            return;
        }
    }
    for (var x = 0; x < ao_uL.length; x++) {
        if (cN.hostname.indexOf(ao_uL[x]) != -1) {
            for (var y = cN.childNodes.length - 1; y >= 0; y--) cN.parentNode.insertBefore(cN.childNodes[y], cN.nextSibling);
            cN.parentNode.removeChild(cN);
            return;
        }
    }
    if (ao_isIE && (cN.childNodes.length == 0 || cN.childNodes[0].nodeType !== 1)) {
        var aCr = document.createElement("acronym");
        while (cN.firstChild) aCr.appendChild(cN.firstChild);
        while (cN.firstChild) cN.removeChild(cN.firstChild);
        cN.appendChild(aCr);
    }
    if (ao_sl_marker_active && cN.className.indexOf("aoSmartTagClass") == -1) {
        var randomID = rdm(10000, 99999);
        if (!cN.hasAttribute("ao_sl_mid")) {
            cN.setAttribute("ao_sl_mid", randomID);
        }
        if (ao_sl_ignore_class && cN.className.indexOf(ao_sl_ignore_class) != -1) {
            return;
        }
        ao_sl_marker_tld_list.push([cN.hostname.replace("www.", ""), randomID]);
        if (AO_MARKER_CHECK_RESULT.length <= 0) {
            return;
        }
    }
    if (!cN.getAttribute('onmousedown')) cN.setAttribute("onmousedown", function (e) {
    });
    if (!cN.getAttribute('onclick')) cN.setAttribute("onclick", function (e) {
    });
    cN.setAttribute("ao_sl_clk", cN.getAttribute('onclick').toString(), 0);
    cN.setAttribute("ao_sl_omd", cN.getAttribute('onmousedown').toString(), 0);
    cN.setAttribute("ao_sl_href", cN.href.toString(), 0);
    if ((cN.getAttribute("rel") == null || cN.getAttribute("rel").indexOf("nofollow") == -1) && ao_isNF) {
        if (cN.getAttribute("rel") == null) {
            cN.setAttribute("rel", "nofollow");
        } else {
            if (cN.getAttribute("rel").indexOf("follow") == -1) {
                cN.setAttribute("rel", cN.getAttribute("rel") + " nofollow");
            } else {
                cN.setAttribute("rel", cN.getAttribute("rel").replace(/(^|\s)follow($|\s)/ig, "nofollow"));
            }
        }
    }
    cN.onmousedown = function (e) {
        try {
            eval(this.getAttribute("ao_sl_omd", 0))[0]();
        } catch (err) {
        }
        if (cN.href.indexOf('http://js.mamydirect.com/redir') == -1) cN.href = ao_ff(this);
    };
    cN.onclick = function (e) {
        var ao_tar = e.target || e.srcElement;
        ao_tar.href = ao_tar.getAttribute('ao_sl_href', 0);
        try {
            eval(this.getAttribute("ao_sl_clk", 0))[0]();
        } catch (err) {
        }
        ao_tar.href = ao_ff(this);
    };
}

function ao_ff(aobj) {
    var ao_q = "";
    if (ao_query != "") ao_q = "&q=" + encodeURIComponent(ao_query);
    var ao_forcesplash = "";
    if (ao_abpc) ao_forcesplash = "&splash=0&abp=1";
    var tag = "";
    if (aobj.className == "aoSmartTagClass") {
        var ao_marketingid = 5;
        tag = aobj.name.split("_")[1];
    } else var ao_marketingid = 1;
    return "http://js.mamydirect.com/redir/clickGate.php?u=RGm1L5B5&m=" + ao_marketingid + "&p=5kCry6GY5B&t=kJlyQUb9&st=" + tag + "&s=" + ao_subid + ao_q + ao_forcesplash + "&url=" + encodeURIComponent(aobj.href) + "&r=" + encodeURIComponent(location.href);
}

function ao_fk(cN, t) {
    var res = Array();
    if (t == 1) {
        if (typeof (ao_st_sec) != "undefined" && ao_st_sec != null && ao_st_sec != "") {
            res = ao_st_sec;
        }
    }
    if (typeof (ao_sl_sec) != "undefined" && ao_sl_sec != null && ao_sl_sec != "") {
        res = res.concat(ao_sl_sec);
    }
    for (var u = 0; u < res.length; u++) {
        if (res[u].n != 1) continue;
        if (res[u].a == "class" && typeof (cN.className.toLowerCase) == 'function') {
            var x = cN.className.toLowerCase().split(" ");
            for (var y = 0; y < x.length; y++) {
                if (x[y] == res[u].v.toLowerCase()) return true;
            }
        } else if (typeof (cN.id.toLowerCase) == 'function') {
            if (cN.id.toLowerCase().substr(0, res[u].v.length) == res[u].v.toLowerCase()) return true;
        }
    }
    return false;
}

function ao_fq(sN) {
    if (sN != "undefined") {
        var chN = sN.childNodes;
        var i = 0;
        while ((i < chN.length) && (chN.length != 0)) {
            var cN = chN[i];
            if (cN.nodeName != "PRE" && cN.nodeType === 1 && cN.childNodes != null && cN.childNodes.length > 0 && ao_ex_el.indexOf(cN.nodeName.toLowerCase() + ',') === -1 && !ao_fk(cN, 1)) {
                if (ao_fq(cN)) return true;
            }
            if (cN.nodeType === 3 && cN.data != '') {
                var parent = cN.parentNode;
                var _x = cN.data;
                var urlPattern = new RegExp("(\\W)(https?:\/\/[^\t $]+)", "ig");
                if (urlPattern.test(cN.data)) {
                    _x = _x.replace(urlPattern, "$1<a rel=\"nofollow\" href=\"$2\" target=\"_blank\">$2</a>");
                }
                if (_x != cN.data) {
                    if (ao_isIE && _x.substr(0, 1) == ' ') {
                        cN.parentNode.insertBefore(document.createTextNode(" "), cN);
                        _x = _x.substr(1);
                    }
                    var _a = document.createElement("div");
                    _a.innerHTML = _x;
                    var _y = document.createDocumentFragment();
                    while (_a.firstChild) _y.appendChild(_a.firstChild);
                    parent.insertBefore(_y, cN);
                    parent.removeChild(cN);
                }
            }
            i++;
        }
    }
}

function ao_fp() {
    ao_gi = true;
    if (typeof (ao_st_sec) == "undefined" || ao_st_sec == null || ao_st_sec == "") {
        if (document.body) return ao_fq(document.body);
    } else {
        var noEntryPoint = true;
        var x = null;
        var res = false;
        for (var u = 0; u < ao_st_sec.length; u++) {
            if (ao_st_sec[u].n == 1) continue;
            x = document.getElementsByTagName(ao_st_sec[u].e);
            for (i = 0; i < x.length; i++) {
                if (ao_st_sec[u].a == "class" && typeof (x[i].className.toLowerCase) == 'function') {
                    if (x[i].className.toLowerCase().substr(0, ao_st_sec[u].v.length) == ao_st_sec[u].v.toLowerCase()) res = ao_fq(x[i]);
                } else {
                    if (typeof (x[i].id.toLowerCase) == 'function') {
                        if (x[i].id.toLowerCase().substr(0, ao_st_sec[u].v.length) == ao_st_sec[u].v.toLowerCase()) res = ao_fq(x[i]);
                    }
                }
                if (res) return true;
            }
        }
        if (noEntryPoint) {
            if (document.body) return ao_fq(document.body);
        }
    }
    return false;
}

function ao_fi() {
    for (var u = 0; u < ao_sl_sec.length; u++) {
        var x = document.getElementsByTagName(ao_sl_sec[u].e);
        for (i = 0; i < x.length; i++) {
            if (ao_sl_sec[u].a == "class" && typeof (x[i].className.toLowerCase) == 'function') {
                if (x[i].className.toLowerCase().substr(0, ao_sl_sec[u].v.length) == ao_sl_sec[u].v.toLowerCase()) {
                    if (ao_sl_sec[u].n == 0) x[i].style.border = "solid 2px green"; else x[i].style.border = "solid 2px red";
                }
            } else if (typeof (x[i].id.toLowerCase) == 'function') {
                if (x[i].id.toLowerCase().substr(0, ao_sl_sec[u].v.length) == ao_sl_sec[u].v.toLowerCase()) {
                    if (ao_sl_sec[u].n == 0) x[i].style.border = "solid 2px green"; else x[i].style.border = "solid 2px red";
                }
            }
        }
    }
}

function ao_fj(f) {
    return f.substr(0, 1).toUpperCase() + f.substr(1);
}

if (ao_isLB) {
    setTimeout("ao_fp()", 600);
}
if (ao_isSL) {
    var ao_reuri = 1;

    function ao_fs() {
        setTimeout(function () {
            if (ao_reuri == 10) return;
            ao_reuri++;
            ao_fc();
            ao_fs();
        }, 500)
    }

    ao_fs();
}

function rdm(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

var ao_gh = null;

function ao_ge(urls) {
    var saoajax = document.createElement("script");
    saoajax.type = "text/javascript";
    saoajax.src = "https://js.smartredirect.de/affiliatemarker/?urls=" + encodeURIComponent(urls);
    var saoajaxinc = document.getElementsByTagName('script')[0];
    saoajaxinc.parentNode.insertBefore(saoajax, saoajaxinc);
    ao_gh = window.setInterval("ao_gd()", 400);
}

function ao_gd() {
    if (AO_MARKER_CHECK_RESULT.length > 0) {
        window.clearInterval(ao_gh);
        for (var i = 0; i < AO_MARKER_CHECK_RESULT.length; i++) {
            if (AO_MARKER_CHECK_RESULT[i][1] == "1") {
                for (var j = 0; j < document.links.length; j++) {
                    if (document.links[j].getAttribute("ao_sl_mid") == AO_MARKER_CHECK_RESULT[i][0][1]) {
                        if (ao_sl_marker != false) {
                            document.links[j].innerHTML += ao_sl_marker;
                        }
                        if (document.links[j].className.length > 0) document.links[j].className += " " + ao_sl_marker_class; else document.links[j].className = ao_sl_marker_class;
                        ao_fe(document.links[j]);
                    }
                }
            }
        }
        AO_MARKER_CHECK_RESULT = [];
        if (ao_sl_marker_info_class && document.getElementsByClassName(ao_sl_marker_info_class).length > 0) {
            var makerElements = document.getElementsByClassName(ao_sl_marker_info_class);
            for (var mE = 0; mE < makerElements.length; mE++) {
                makerElements[mE].style.display = "inline-block";
            }
        }
    }
}