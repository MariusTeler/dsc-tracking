// Script pentru funcționalitate suplimentară (opțional)

document.addEventListener('DOMContentLoaded', function() {
    // Animație pentru progress cards
    const progressCards = document.querySelectorAll('.row.g-2.g-lg-4 .col-6');

    progressCards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            card.style.transition = 'all 0.5s ease';

            setTimeout(() => {
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, 100);
        }, index * 100);
    });

    // Animație pentru timeline items
    const timelineItems = document.querySelectorAll('.timeline-item');

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateX(0)';
            }
        });
    }, observerOptions);

    timelineItems.forEach((item, index) => {
        item.style.opacity = '0';
        item.style.transform = 'translateX(-20px)';
        item.style.transition = 'all 0.5s ease';
        item.style.transitionDelay = `${index * 0.1}s`;
        observer.observe(item);
    });

    // Auto-focus pe input field
    const awbInput = document.getElementById('awb');
    if (awbInput) {
        awbInput.focus();
    }

    // Validare AWB (doar cifre)
    const awbInputs = document.querySelectorAll('input[name="awb"]');
    awbInputs.forEach(input => {
        input.addEventListener('input', function(e) {
            // Permite doar cifre
            this.value = this.value.replace(/[^0-9]/g, '');
        });
    });

    // Smooth scroll pentru timeline
    const timelineContainer = document.querySelector('.timeline');
    if (timelineContainer) {
        timelineContainer.style.scrollBehavior = 'smooth';
    }

    // Optional: AJAX tracking update (pentru refresh automat)
    function updateTracking(awb) {
        fetch(`/api/tracking/${awb}`)
            .then(response => response.json())
            .then(data => {
                console.log('Tracking updated:', data);
                // Aici poți actualiza UI-ul fără refresh
            })
            .catch(error => console.error('Error:', error));
    }

    // Uncomment pentru auto-refresh la fiecare 30 secunde
    // const currentAwb = new URLSearchParams(window.location.search).get('awb');
    // if (currentAwb) {
    //     setInterval(() => updateTracking(currentAwb), 30000);
    // }
});
