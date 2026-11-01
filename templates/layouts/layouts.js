/* ============================================================
   layouts.js — animacao por layout (GSAP, sem plugin pago)
   Contrato: docs/ARQUITETURA.md §2/§3   Spec: docs/LAYOUTS.md §10

   Cada funcao recebe (root, tl, t, dur, start):
     root  = <section> da cena
     tl    = timeline mestre (paused, montada pelo gerador)
     t     = inicio da entrada do texto (start + entrada_offset)
     dur   = duracao da cena em segundos
     start = inicio da cena (para efeitos de fim de cena)

   Regras:
     - o gerador so inclui este arquivo se houver cena com `tipo`;
     - `texto` reproduz o v1 exatamente (base);
     - so transform/opacity animados; nada de filtro em area cheia;
     - todo layout chama base() ou define a entrada do texto por conta propria.
   ============================================================ */
(function () {
  "use strict";

  var q = function (root, sel) { return root.querySelector(sel); };
  var qa = function (root, sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); };

  /* ---------- v1: entrada padrao do texto ---------- */
  function base(root, tl, t) {
    var h1 = q(root, "h1");
    if (h1) tl.from(h1, { opacity: 0, y: 36, duration: 0.55, ease: "power2.out" }, t);
    var accent = q(root, ".accent");
    if (accent) tl.from(accent, { scaleX: 0, duration: 0.5, ease: "power2.out" }, t + 0.10);
    var small = q(root, ".small");
    if (small) tl.from(small, { opacity: 0, y: 14, duration: 0.45, ease: "power2.out" }, t + 0.18);
    var kicker = q(root, ".kicker");
    if (kicker) tl.from(kicker, { opacity: 0, duration: 0.4, ease: "power1.out" }, t + 0.05);
  }

  var L = {};
  L.texto = base;

  /* ---------- 1. ORBIT ---------- */
  L.orbit = function (root, tl, t, dur) {
    base(root, tl, t);
    var ring = q(root, ".ring");
    var orbs = qa(root, ".orb");
    var decor = q(root, ".ly-decor");
    if (decor) tl.from(decor, { opacity: 0, duration: 0.6, ease: "power1.out" }, t);
    if (ring) {
      tl.from(ring, { rotation: -26, duration: 1.0, ease: "power2.out" }, t);
      tl.to(ring, { rotation: 62, duration: Math.max(0.6, dur - 0.4), ease: "none" }, t + 0.4);
    }
    orbs.forEach(function (o, i) {
      tl.from(o, { scale: 0, duration: 0.5, ease: "back.out(2.2)" }, t + 0.1 + i * 0.08);
    });
  };

  /* ---------- 2. COUCH WALL ---------- */
  L["couch-wall"] = function (root, tl, t, dur) {
    base(root, tl, t);
    var wall = q(root, ".wall");
    var cards = qa(root, ".wall span");
    if (wall) tl.fromTo(wall, { y: 40 }, { y: -40, duration: Math.max(1, dur), ease: "none" }, t);
    cards.forEach(function (c, i) {
      tl.from(c, { opacity: 0, scale: 0.94, duration: 0.5, ease: "power2.out" }, t + i * 0.035);
    });
    var scrim = q(root, ".scrim");
    if (scrim) tl.from(scrim, { opacity: 0, duration: 0.7, ease: "power1.out" }, t);
  };

  /* ---------- 3. UI WORLD ---------- */
  L["ui-world"] = function (root, tl, t, dur) {
    var win = q(root, ".win");
    var body = q(root, ".body");
    if (win) {
      tl.from(win, { opacity: 0, scale: 0.95, y: 26, duration: 0.7, ease: "power3.out" }, t);
      tl.from(q(root, ".bar"), { opacity: 0, duration: 0.4 }, t + 0.15);
    }
    base(root, tl, t + 0.22);
    if (body) tl.from(body, { opacity: 0.4, duration: 0.6 }, t + 0.22);
    var url = q(root, ".url");
    if (url) tl.from(url, { opacity: 0, duration: 0.4 }, t + 0.35);
    if (win) tl.to(win, { scale: 1.02, duration: Math.max(0.5, dur - 1), ease: "none" }, t + 0.8);
  };

  /* ---------- 4. FRAME BREAK ---------- */
  L["frame-break"] = function (root, tl, t, dur) {
    var f = q(root, ".fb-frame");
    if (f) {
      tl.from(f, { scaleX: 0, duration: 0.45, ease: "power2.out" }, t);
      tl.from(f, { scaleY: 0, duration: 0.45, ease: "power2.out" }, t + 0.22);
    }
    var mask = q(root, ".fb-mask");
    if (mask) tl.from(mask, { opacity: 0, duration: 0.5 }, t + 0.4);
    var h1 = q(root, "h1");
    if (h1) {
      tl.from(h1, { opacity: 0, scale: 0.86, duration: 0.6, ease: "back.out(1.6)" }, t + 0.4);
      tl.to(h1, { scale: 1.06, duration: Math.max(0.5, dur - 1), ease: "none" }, t + 1.0);
    }
    var kicker = q(root, ".kicker");
    if (kicker) tl.from(kicker, { opacity: 0, duration: 0.4 }, t + 0.3);
    var small = q(root, ".small");
    if (small) tl.from(small, { opacity: 0, y: 14, duration: 0.45, ease: "power2.out" }, t + 0.62);
    var accent = q(root, ".accent");
    if (accent) tl.from(accent, { scaleX: 0, duration: 0.5, ease: "power2.out" }, t + 0.5);
  };

  /* ---------- 5. DIGITAL ZOOM ---------- */
  L["digital-zoom"] = function (root, tl, t, dur) {
    base(root, tl, t);
    var core = q(root, ".core");
    if (core) tl.fromTo(core, { scale: 1 }, { scale: 1.12, duration: Math.max(0.8, dur * 0.8), ease: "steps(6)" }, t + 0.15);
  };

  /* ---------- 6. PHONE MOCKUP ---------- */
  L["phone-mockup"] = function (root, tl, t, dur) {
    var phone = q(root, ".phone");
    if (phone) {
      tl.from(phone, { opacity: 0, y: 70, rotation: -3, duration: 0.85, ease: "power3.out" }, t);
      tl.to(phone, { y: -18, duration: Math.max(0.6, dur - 0.9), ease: "none" }, t + 0.85);
    }
    base(root, tl, t + 0.28);
  };

  /* ---------- 7. CHECKLIST ---------- */
  L["checklist"] = function (root, tl, t, dur) {
    var h1 = q(root, "h1");
    if (h1) tl.from(h1, { opacity: 0, y: 30, duration: 0.5, ease: "power2.out" }, t);
    var kicker = q(root, ".kicker");
    if (kicker) tl.from(kicker, { opacity: 0, duration: 0.4 }, t + 0.05);
    var small = q(root, ".small");
    if (small) tl.from(small, { opacity: 0, y: 12, duration: 0.4 }, t + 0.12);
    qa(root, ".item").forEach(function (it, i) {
      var at = t + 0.26 + i * 0.22;
      tl.from(it, { opacity: 0, x: -34, duration: 0.42, ease: "power2.out" }, at);
      var path = q(it, "path");
      if (path) tl.to(path, { strokeDashoffset: 0, duration: 0.3, ease: "power1.inOut" }, at + 0.2);
    });
  };

  /* ---------- 8. HEADLINE WALL ---------- */
  L["headline-wall"] = function (root, tl, t, dur) {
    var rows = qa(root, ".wall span");
    rows.forEach(function (r, i) {
      var dir = i % 2 === 0 ? 1 : -1;
      tl.from(r, { opacity: 0, duration: 0.5, ease: "power1.out" }, t + i * 0.05);
      tl.fromTo(r, { x: -70 * dir }, { x: 70 * dir, duration: Math.max(1, dur), ease: "none" }, t);
    });
    var scrim = q(root, ".scrim");
    if (scrim) tl.from(scrim, { opacity: 0, duration: 0.7 }, t);
    base(root, tl, t + 0.1);
  };

  /* ---------- 9. ZOOM THROUGH ---------- */
  L["zoom-through"] = function (root, tl, t, dur, start) {
    base(root, tl, t);
    var core = q(root, ".core");
    if (core) {
      var fim = Math.max(t + 0.6, start + dur - 0.45);
      tl.to(core, { scale: 5.2, opacity: 0, duration: 0.45, ease: "power3.in" }, fim);
    }
  };

  /* ---------- 10. CHART GROW ---------- */
  L["chart-grow"] = function (root, tl, t, dur) {
    var h1 = q(root, "h1");
    if (h1) tl.from(h1, { opacity: 0, y: 28, duration: 0.5, ease: "power2.out" }, t);
    var kicker = q(root, ".kicker");
    if (kicker) tl.from(kicker, { opacity: 0, duration: 0.4 }, t + 0.05);
    var small = q(root, ".small");
    if (small) tl.from(small, { opacity: 0, y: 12, duration: 0.4 }, t + 0.1);
    qa(root, ".bar").forEach(function (bar, i) {
      var at = t + 0.3 + i * 0.14;
      var b = q(bar, "b");
      if (b) tl.from(b, { scaleY: 0, duration: 0.62, ease: "power2.out" }, at);
      var u = q(bar, "u");
      var alvo = u ? parseInt(u.getAttribute("data-valor") || "0", 10) : 0;
      if (u) {
        var cont = { v: 0 };
        tl.to(cont, {
          v: alvo, duration: 0.7, ease: "power1.out", snap: { v: 1 },
          onUpdate: function () { u.textContent = String(cont.v); }
        }, at);
        tl.set(u, { textContent: String(alvo) }, at + 0.72);
      }
      var i2 = q(bar, "i");
      if (i2) tl.from(i2, { opacity: 0, duration: 0.35 }, at + 0.1);
    });
  };

  /* ---------- 11. PULL BACK ---------- */
  L["pull-back"] = function (root, tl, t, dur) {
    var core = q(root, ".core");
    if (core) {
      tl.from(core, { scale: 1.55, y: -30, duration: 1.0, ease: "power3.out" }, t);
      tl.to(core, { scale: 1.0, y: 0, duration: Math.max(0.4, dur - 1.1), ease: "none" }, t + 1.0);
    }
    var h1 = q(root, "h1");
    if (h1) tl.from(h1, { opacity: 0, duration: 0.45, ease: "power2.out" }, t);
    var kicker = q(root, ".kicker");
    if (kicker) tl.from(kicker, { opacity: 0, duration: 0.4 }, t + 0.2);
    var small = q(root, ".small");
    if (small) tl.from(small, { opacity: 0, y: 16, duration: 0.5, ease: "power2.out" }, t + 0.75);
    var accent = q(root, ".accent");
    if (accent) tl.from(accent, { scaleX: 0, duration: 0.5, ease: "power2.out" }, t + 0.85);
  };

  /* ---------- 12. GREEN SCREEN ---------- */
  L["green-screen"] = function (root, tl, t, dur) {
    var key = q(root, ".key");
    if (key) {
      tl.from(key, { opacity: 0, y: 60, duration: 0.8, ease: "power2.out" }, t);
      tl.to(key, { scale: 1.04, duration: Math.max(0.6, dur - 0.8), ease: "none" }, t + 0.8);
    }
    var line = q(root, ".keyline");
    if (line) tl.from(line, { opacity: 0, duration: 0.6 }, t + 0.3);
    base(root, tl, t + 0.2);
  };

  /* ---------- 13. PAPER CUT ---------- */
  L["paper-cut"] = function (root, tl, t, dur) {
    var layers = qa(root, ".layer");
    layers.forEach(function (l, i) {
      var dir = i % 2 === 0 ? 1 : -1;
      var amp = 26 + i * 16;
      tl.from(l, { opacity: 0, duration: 0.5, ease: "power1.out" }, t + i * 0.08);
      tl.fromTo(l, { x: -amp * dir }, { x: amp * dir, duration: Math.max(1, dur), ease: "none" }, t);
    });
    base(root, tl, t + 0.12);
  };

  /* ---------- 14. DOODLE BOIL ---------- */
  L["doodle-boil"] = function (root, tl, t, dur) {
    base(root, tl, t);
    var svgs = qa(root, ".boil svg");
    if (!svgs.length) return;
    var paths = svgs.map(function (s) { return q(s, "path"); });
    svgs.forEach(function (s, i) { tl.set(s, { autoAlpha: i === 0 ? 1 : 0 }, 0); });
    paths.forEach(function (p) {
      if (p) tl.to(p, { strokeDashoffset: 0, duration: 0.55, ease: "power1.inOut" }, t + 0.35);
    });
    var passo = 0.1;
    var quadros = Math.max(1, Math.floor((dur - 1.0) / passo));
    for (var k = 0; k < quadros; k++) {
      var at = t + 0.95 + k * passo;
      tl.set(svgs, { autoAlpha: 0 }, at);
      tl.set(svgs[k % svgs.length], { autoAlpha: 1 }, at);
    }
  };

  /* ---------- 15. VERTIGO ---------- */
  L.vertigo = function (root, tl, t, dur) {
    base(root, tl, t);
    var core = q(root, ".core");
    var decor = q(root, ".ly-decor");
    if (core) tl.fromTo(core, { scale: 1.0, rotation: 0 }, { scale: 1.2, rotation: -1.2, duration: Math.max(1, dur), ease: "none" }, t);
    if (decor) {
      tl.from(decor, { opacity: 0, duration: 0.6 }, t);
      tl.fromTo(decor, { scale: 1.16, rotation: 2 }, { scale: 1.0, rotation: 0, duration: Math.max(1, dur), ease: "none" }, t);
    }
  };

  /* ---------- 16. COVER STORY ---------- */
  L["cover-story"] = function (root, tl, t, dur) {
    var cover = q(root, ".cover");
    if (cover) {
      tl.from(cover, { opacity: 0, y: 44, duration: 0.75, ease: "power3.out" }, t);
      tl.to(cover, { y: -14, duration: Math.max(0.6, dur - 0.8), ease: "none" }, t + 0.75);
    }
    var mast = q(root, ".masthead");
    if (mast) tl.from(mast, { opacity: 0, y: 18, duration: 0.5, ease: "power2.out" }, t + 0.2);
    var rule = q(root, ".rule");
    if (rule) tl.from(rule, { scaleX: 0, duration: 0.5, ease: "power2.out" }, t + 0.45);
    var issue = q(root, ".issue");
    if (issue) tl.from(issue, { opacity: 0, duration: 0.4 }, t + 0.55);
    var bar = q(root, ".barcode");
    if (bar) tl.from(bar, { scaleX: 0, duration: 0.45, ease: "power2.out" }, t + 0.6);
    var call = q(root, ".call");
    if (call) tl.from(call, { opacity: 0, duration: 0.4 }, t + 0.7);
    base(root, tl, t + 0.3);
  };

  /* ---------- 17. GLASS TYPE ---------- */
  L["glass-type"] = function (root, tl, t, dur) {
    var pane = q(root, ".pane");
    if (pane) {
      tl.from(pane, { opacity: 0, scale: 0.965, duration: 0.7, ease: "power2.out" }, t);
      tl.to(pane, { y: -12, duration: Math.max(0.6, dur - 0.8), ease: "none" }, t + 0.8);
    }
    base(root, tl, t + 0.18);
  };

  window.__layouts = L;
})();
