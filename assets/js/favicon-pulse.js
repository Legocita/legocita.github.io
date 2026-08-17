/* Gentle pulsing favicon — Legocita Makes
   Draws the strawberry "L" monogram to a small canvas and softly scales it
   in and out, updating the tab icon a few times a second. Subtle by design:
   ~93%–100% scale over a slow ~2.5s cycle. Falls back silently to the
   static favicon-static.png if canvas/JS isn't available. */
(function () {
  function start() {
    var link = document.querySelector("link[rel~='icon']");
    if (!link) {
      link = document.createElement('link');
      link.rel = 'icon';
      document.head.appendChild(link);
    }
    link.type = 'image/png';

    var img = new Image();
    img.onload = function () {
      var size = 64;
      var canvas = document.createElement('canvas');
      canvas.width = size;
      canvas.height = size;
      var ctx = canvas.getContext('2d');
      var t = 0;

      function tick() {
        t += 0.10;
        var scale = 0.93 + 0.07 * (0.5 + 0.5 * Math.sin(t));
        var w = size * scale, h = size * scale;
        ctx.clearRect(0, 0, size, size);
        ctx.drawImage(img, (size - w) / 2, (size - h) / 2, w, h);
        link.href = canvas.toDataURL('image/png');
      }

      tick();
      setInterval(tick, 110);
    };
    img.onerror = function () {
      link.href = '/assets/images/favicon-static.png';
    };
    img.src = '/assets/images/favicon-strawberry.png';
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
})();
