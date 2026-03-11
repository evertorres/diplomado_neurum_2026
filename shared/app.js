window.initApp = function () {
    // --- Slide Navigation Logic ---
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.getElementById('prevSlide');
    const nextBtn = document.getElementById('nextSlide');
    const counterEl = document.getElementById('slideCounter');

    let currentSlide = 0;
    const totalSlides = slides.length;

    // Use URL hash for initial slide if present
    if (window.location.hash) {
        const hashSlide = parseInt(window.location.hash.substring(1));
        if (!isNaN(hashSlide) && hashSlide > 0 && hashSlide <= totalSlides) {
            currentSlide = hashSlide - 1;
        }
    }

    function updateSlides() {
        if (!slides || slides.length === 0) return;

        slides.forEach((slide, index) => {
            slide.classList.remove('active', 'prev');
            if (index === currentSlide) {
                slide.classList.add('active');
            } else if (index < currentSlide) {
                slide.classList.add('prev');
            }
        });

        if (counterEl) {
            counterEl.textContent = `${currentSlide + 1} / ${totalSlides}`;
        }

        if (prevBtn) prevBtn.disabled = currentSlide === 0;
        if (nextBtn) nextBtn.disabled = currentSlide === totalSlides - 1;

        // Update URL hash without breaking history, making slides shareable
        history.replaceState(null, null, `#${currentSlide + 1}`);
    }

    // Keyboard navigation
    // Use a named function to prevent duplicate listeners
    function handleKeyDown(e) {
        if (e.key === 'ArrowRight' || e.key === 'Space' || e.key === 'Enter') {
            if (currentSlide < totalSlides - 1) {
                currentSlide++;
                updateSlides();
            }
        } else if (e.key === 'ArrowLeft') {
            if (currentSlide > 0) {
                currentSlide--;
                updateSlides();
            }
        }
    }

    document.removeEventListener('keydown', window._handleKeyDown || (() => { }));
    window._handleKeyDown = handleKeyDown;
    document.addEventListener('keydown', window._handleKeyDown);

    // --- Navigate via Buttons ---
    // Event delegation on document to avoid losing references
    document.removeEventListener('click', window._handleNavClick || (() => { }));

    window._handleNavClick = function (e) {
        const targetBtn = e.target.closest('button.control-btn');
        if (!targetBtn) return;

        if (targetBtn.id === 'prevSlide') {
            if (currentSlide > 0) {
                currentSlide--;
                updateSlides();
            }
        }
        else if (targetBtn.id === 'nextSlide') {
            if (currentSlide < totalSlides - 1) {
                currentSlide++;
                updateSlides();
            }
        }
    };

    document.addEventListener('click', window._handleNavClick);

    // Initialize display
    updateSlides();


    // --- Modal Logic ---
    const modalTriggers = document.querySelectorAll('[data-modal-target]');
    const overlays = document.querySelectorAll('.modal-overlay');
    const closeBtns = document.querySelectorAll('.modal-close');

    function openModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.add('active');
            // Prevent body scroll
            document.body.style.overflow = 'hidden';

            // Allow clicking outside the modal content to close
            const outsideClick = (e) => {
                if (e.target === modal) {
                    closeModal(modalId);
                    modal.removeEventListener('click', outsideClick);
                }
            };
            modal.addEventListener('click', outsideClick);
        }
    }

    function closeModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }
    }

    modalTriggers.forEach(trigger => {
        // Clone to remove old listeners
        const newTrigger = trigger.cloneNode(true);
        trigger.parentNode.replaceChild(newTrigger, trigger);
        newTrigger.addEventListener('click', () => {
            const target = newTrigger.getAttribute('data-modal-target');
            openModal(target);
        });
    });

    closeBtns.forEach(btn => {
        const newBtn = btn.cloneNode(true);
        btn.parentNode.replaceChild(newBtn, btn);
        newBtn.addEventListener('click', (e) => {
            const modal = e.target.closest('.modal-overlay');
            if (modal) {
                closeModal(modal.id);
            }
        });
    });

    // Handle Escape key to close modals
    function handleEscape(e) {
        if (e.key === 'Escape') {
            const activeModal = document.querySelector('.modal-overlay.active');
            if (activeModal) {
                closeModal(activeModal.id);
            }
        }
    }
    document.removeEventListener('keydown', window._handleEscape || (() => { }));
    window._handleEscape = handleEscape;
    document.addEventListener('keydown', window._handleEscape);

    // --- Global Image Zoom Modals ---
    const zoomableImages = document.querySelectorAll('.zoomable-image');
    const globalImageModal = document.getElementById('global-image-modal');
    const globalImageContent = document.getElementById('global-image-content');

    if (globalImageModal && globalImageContent) {
        zoomableImages.forEach(img => {
            const newImg = img.cloneNode(true);
            img.parentNode.replaceChild(newImg, img);
            newImg.addEventListener('click', () => {
                globalImageContent.src = newImg.src;
                openModal('global-image-modal');
            });
        });
    }
};

document.addEventListener('DOMContentLoaded', () => {
    // If not dynamically loading, init immediately
    if (document.querySelectorAll('.slide').length > 0) {
        window.initApp();
    }
});
