/* ============================================================
   INDEX.JS - Página de Links/Bio
   ============================================================ */

document.addEventListener('DOMContentLoaded', function() {
    // Animate links on load with stagger
    const links = document.querySelectorAll('.link-button');
    links.forEach((link, index) => {
        link.style.opacity = '0';
        link.style.transform = 'translateY(20px)';
        setTimeout(() => {
            link.style.transition = 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)';
            link.style.opacity = '1';
            link.style.transform = 'translateY(0)';
        }, 100 + (index * 80));
    });

    // Social icons animation
    const socials = document.querySelectorAll('.social-links a');
    socials.forEach((social, index) => {
        social.style.opacity = '0';
        social.style.transform = 'scale(0.8)';
        setTimeout(() => {
            social.style.transition = 'all 0.3s ease';
            social.style.opacity = '0.75';
            social.style.transform = 'scale(1)';
        }, 600 + (index * 100));
    });

    // Track link clicks (analytics placeholder)
    document.querySelectorAll('.link-button').forEach(button => {
        button.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href && !href.startsWith('http')) {
                // Internal link - smooth navigation
                return;
            }
            // External link - could add analytics here
            console.log('Link clicked:', href);
        });
    });
});
