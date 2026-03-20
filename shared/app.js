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

    // Helper function to handle forward progression of fragments
    function advanceFragments(currentSlideEl) {
        const nonVisibleFragments = currentSlideEl.querySelectorAll('.fragment:not(.visible)');
        if (nonVisibleFragments.length > 0) {
            let minIndex = Infinity;
            nonVisibleFragments.forEach(f => {
                const idx = parseInt(f.getAttribute('data-fragment-index') || Number.MAX_SAFE_INTEGER);
                if (idx < minIndex) minIndex = idx;
            });
            nonVisibleFragments.forEach(f => {
                const idx = parseInt(f.getAttribute('data-fragment-index') || Number.MAX_SAFE_INTEGER);
                if (idx === minIndex) f.classList.add('visible');
            });
            return true; // Advanced a fragment
        }
        return false; // No more fragments to advance
    }

    // Helper function to handle backward progression of fragments
    function retreatFragments(currentSlideEl) {
        const visibleFragments = currentSlideEl.querySelectorAll('.fragment.visible');
        if (visibleFragments.length > 0) {
            let maxIndex = -Infinity;
            visibleFragments.forEach(f => {
                const idx = parseInt(f.getAttribute('data-fragment-index') || -1);
                if (idx > maxIndex) maxIndex = idx;
            });
            visibleFragments.forEach(f => {
                const idx = parseInt(f.getAttribute('data-fragment-index') || -1);
                if (idx === maxIndex) f.classList.remove('visible');
            });
            return true; // Retreated a fragment
        }
        return false; // No more fragments to retreat
    }

    // Keyboard navigation
    // Use a named function to prevent duplicate listeners
    function handleKeyDown(e) {
        if (e.key === 'ArrowRight' || e.key === 'Space' || e.key === 'Enter') {
            const currentSlideEl = slides[currentSlide];
            if (!advanceFragments(currentSlideEl) && currentSlide < totalSlides - 1) {
                // No more fragments, go to next slide
                currentSlide++;
                updateSlides();
            }
        } else if (e.key === 'ArrowLeft') {
            const currentSlideEl = slides[currentSlide];
            if (!retreatFragments(currentSlideEl) && currentSlide > 0) {
                // No more visible fragments, go to prev slide
                currentSlide--;
                updateSlides();
                
                // When going backwards to a slide, show all its fragments
                setTimeout(() => {
                    const prevSlideEl = slides[currentSlide];
                    const allFragments = prevSlideEl.querySelectorAll('.fragment');
                    allFragments.forEach(f => f.classList.add('visible'));
                }, 10);
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
        const targetBtn = e.target.closest('.control-btn');
        const currentSlideEl = slides[currentSlide];
        
        if (!targetBtn) {
            // Check if clicking on the slide container to advance presentation
            const slideContainer = e.target.closest('.presentation-container');
            // Don't advance if clicking on interactive elements
            const isInteractive = e.target.closest('button, a, input, .modal, .zoomable-image, [data-modal-target], .slide-controls');
            
            if (slideContainer && !isInteractive && currentSlideEl) {
                if (!advanceFragments(currentSlideEl) && currentSlide < totalSlides - 1) {
                    currentSlide++;
                    updateSlides();
                }
            }
            return;
        }

        if (targetBtn.id === 'prevSlide' && currentSlideEl) {
            if (!retreatFragments(currentSlideEl) && currentSlide > 0) {
                currentSlide--;
                updateSlides();
                setTimeout(() => {
                    const newSlideEl = slides[currentSlide];
                    if (newSlideEl) {
                        newSlideEl.querySelectorAll('.fragment').forEach(f => f.classList.add('visible'));
                    }
                }, 10);
            }
        }
        else if (targetBtn.id === 'nextSlide' && currentSlideEl) {
            if (!advanceFragments(currentSlideEl) && currentSlide < totalSlides - 1) {
                currentSlide++;
                updateSlides();
            }
        }
    };

    document.addEventListener('click', window._handleNavClick);

    // Initialize display
    updateSlides();
    
    // Reset fragments on the first slide if any
    slides[currentSlide].querySelectorAll('.fragment').forEach(f => f.classList.remove('visible'));


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
    // --- Interactive Sliders ---
    const dikwSlider = document.getElementById('dikw-slider');
    if (dikwSlider) {
        const img0 = document.getElementById('slide5-img0');
        const img1 = document.getElementById('slide5-img1');
        const img2 = document.getElementById('slide5-img2');
        const img3 = document.getElementById('slide5-img3');
        const img4 = document.getElementById('slide5-img4');
        const img5 = document.getElementById('slide5-img5');

        // Prevent slide navigation when using the slider range
        dikwSlider.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowRight' || e.key === 'ArrowLeft' || e.key === 'Space') {
                e.stopPropagation();
            }
        });

        dikwSlider.addEventListener('input', function() {
            const val = parseFloat(this.value);
            
            // Image 0 fades in between 0.0 and 1.0
            if (img0) img0.style.opacity = Math.max(0, Math.min(1, val));
            
            // Image 1 fades in between 1.0 and 2.0
            if (img1) img1.style.opacity = Math.max(0, Math.min(1, val - 1));
            
            // Image 2 fades in between 2.0 and 3.0
            if (img2) img2.style.opacity = Math.max(0, Math.min(1, val - 2));
            
            // Image 3 fades in between 3.0 and 4.0
            if (img3) img3.style.opacity = Math.max(0, Math.min(1, val - 3));
            
            // Image 4 fades in between 4.0 and 5.0
            if (img4) img4.style.opacity = Math.max(0, Math.min(1, val - 4));
            
            // Image 5 fades in between 5.0 and 6.0
            if (img5) img5.style.opacity = Math.max(0, Math.min(1, val - 5));
        });
    }

    // --- Interoperability Slider (Slide 02) ---
    const interopSlider = document.getElementById('interop-slider');
    if (interopSlider) {
        const img1 = document.getElementById('slide2-img1');
        const img2 = document.getElementById('slide2-img2');

        interopSlider.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
                e.stopPropagation();
            }
        });

        interopSlider.addEventListener('input', function() {
            const val = parseFloat(this.value);
            // img1 (Sistemas) fades in between 0.0 and 1.0
            if (img1) img1.style.opacity = Math.max(0, Math.min(1, val));
            // img2 (Conectividad) fades in between 1.0 and 2.0
            if (img2) img2.style.opacity = Math.max(0, Math.min(1, val - 1));
        });

        // Scroll (wheel) to change slider value for "scroll-to-swap" effect
        const slideArea = interopSlider.closest('.slide');
        if (slideArea) {
            slideArea.addEventListener('wheel', function(e) {
                e.preventDefault();
                const delta = e.deltaY;
                const factor = 0.002; // Sensibilidad del scroll
                let newVal = parseFloat(interopSlider.value) + (delta * factor);
                newVal = Math.max(0, Math.min(2, newVal));
                interopSlider.value = newVal;
                interopSlider.dispatchEvent(new Event('input'));
            }, { passive: false });
        }
    }
};

document.addEventListener('DOMContentLoaded', () => {
    // If not dynamically loading, init immediately
    if (document.querySelectorAll('.slide').length > 0) {
        window.initApp();
    }
});
