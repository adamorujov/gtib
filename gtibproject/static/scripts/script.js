const introGalleryMain = document.querySelector('.intro__gallery-main img')
const introGallerySub = document.querySelectorAll('.intro__gallery-sub img')

introGallerySub.forEach((image, index) => {
    image.addEventListener('click', (e) => {
        let mainImageSource = introGalleryMain.getAttribute('src')
        let subImageSource = e.target.getAttribute('src')

        e.target.setAttribute('src', mainImageSource)
        introGalleryMain.setAttribute('src', subImageSource)
    })
})

const accordionBtn = document.querySelectorAll('.faq__item h2')

accordionBtn.forEach((btn) => {
    btn.addEventListener('click', (e) => {

        if(e.target.parentNode.querySelector('.faq__panel').style.display == 'block') {
            e.target.parentNode.querySelector('.faq__panel').style.display = 'none'
            e.target.querySelector('i').classList.remove('fa-chevron-down')
            e.target.querySelector('i').classList.add('fa-chevron-up')
        }else {
            e.target.parentNode.querySelector('.faq__panel').style.display = 'block'
            e.target.querySelector('i').classList.add('fa-chevron-down')
            e.target.querySelector('i').classList.remove('fa-chevron-up')
        }

    })
})

const mobileNavBtn = document.querySelectorAll('.nav__mobile-link')

mobileNavBtn.forEach((btn) => {
    btn.addEventListener('click', (e) => {
        if(e.target.parentNode.querySelector('.nav__mobile-sublinks').style.display == 'flex') {
            e.target.parentNode.querySelector('.nav__mobile-sublinks').style.display = 'none'
        }else {
            e.target.parentNode.parentNode.querySelectorAll('.nav__mobile-sublinks').forEach((a) => a.style.display = 'none')
            e.target.parentNode.querySelector('.nav__mobile-sublinks').style.display = 'flex'
            
        }
    })
})

document.querySelector('.nav__mobile-btn').addEventListener('click', () => {
        document.querySelector('.nav__mobile').style.display = 'block'
})

document.querySelector('.logout').addEventListener('click', () => {
    document.querySelector('.nav__mobile').style.display = 'none'
})