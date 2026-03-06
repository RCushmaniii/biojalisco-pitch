"""Diagnose team carousel issues on mobile"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 375, "height": 812})
    page.goto("http://localhost:8080")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(1000)

    btn = page.locator("text=Browse Freely")
    if btn.is_visible():
        btn.click()
        page.wait_for_timeout(800)

    # Scroll to team section
    page.evaluate("document.getElementById('team').scrollIntoView({behavior:'instant'})")
    page.wait_for_timeout(500)

    info = page.evaluate("""() => {
        var section = document.getElementById('team');
        var sectionR = section.getBoundingClientRect();
        var grid = section.querySelector('.roles-grid');
        var gridR = grid.getBoundingClientRect();
        var dots = section.querySelector('.team-dots');
        var dotsR = dots ? dots.getBoundingClientRect() : null;
        var cards = grid.querySelectorAll('.role-card');
        var cardRects = [];
        cards.forEach(function(c) {
            var r = c.getBoundingClientRect();
            cardRects.push({ top: r.top, bottom: r.bottom, height: r.height, left: r.left, width: r.width });
        });
        return {
            viewport: window.innerHeight,
            sectionTop: sectionR.top,
            sectionHeight: sectionR.height,
            sectionBottom: sectionR.bottom,
            gridTop: gridR.top,
            gridBottom: gridR.bottom,
            gridHeight: gridR.height,
            gridScrollWidth: grid.scrollWidth,
            gridClientWidth: grid.clientWidth,
            dotsTop: dotsR ? dotsR.top : null,
            dotsBottom: dotsR ? dotsR.bottom : null,
            dotsVisible: dotsR ? (dotsR.top < window.innerHeight && dotsR.bottom > 0) : false,
            dotsHeight: dotsR ? dotsR.height : 0,
            cards: cardRects
        };
    }""")

    print("=== Team Section Layout ===")
    print(f"  Viewport: {info['viewport']}px")
    print(f"  Section: top={info['sectionTop']:.0f}, height={info['sectionHeight']:.0f}, bottom={info['sectionBottom']:.0f}")
    print(f"  Grid: top={info['gridTop']:.0f}, bottom={info['gridBottom']:.0f}, height={info['gridHeight']:.0f}")
    print(f"  Grid scroll: scrollWidth={info['gridScrollWidth']:.0f}, clientWidth={info['gridClientWidth']:.0f}")
    print(f"  Dots: top={info['dotsTop']}, bottom={info['dotsBottom']}, visible={info['dotsVisible']}")
    for i, c in enumerate(info['cards']):
        print(f"  Card {i}: top={c['top']:.0f}, bottom={c['bottom']:.0f}, height={c['height']:.0f}, left={c['left']:.0f}, width={c['width']:.0f}")

    # Check if dots are below the fold
    if info['dotsTop'] and info['dotsTop'] > info['viewport']:
        print(f"\n  PROBLEM: Dots are {info['dotsTop'] - info['viewport']:.0f}px BELOW viewport fold!")

    page.screenshot(path="/tmp/team_debug.png", full_page=False)

    # Also scroll to show dots area
    page.evaluate("document.querySelector('.team-dots').scrollIntoView({behavior:'instant', block:'center'})")
    page.wait_for_timeout(300)
    page.screenshot(path="/tmp/team_dots_visible.png", full_page=False)

    browser.close()
