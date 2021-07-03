import Head from 'next/head'
import styles from '../styles/Home.module.css'

// import dynamic from 'next/dynamic'

import Controller from './controller'

// const Controller = dynamic(() => import('./controller'))

function makeAnalyticsScript(id) {
    return `window.dataLayer = window.dataLayer || [];
              function gtag(){dataLayer.push(arguments);}
              gtag('js', new Date());
              gtag('config', '${id}', { page_path: window.location.pathname });`
}


export default function Home() {

    return (
        <div className={styles.container}>
            <Head>
                <title>Multimaze by Beren Gunsolus</title>
                <meta name="viewport" content="width=device-width, initial-scale=1"/>
                <link rel="icon" href="/favicon.ico"/>
                <script dangerouslySetInnerHTML={{
                    __html: `
                        const gaId = typeof window !== 'undefined' && window.location.toString().includes('hardestmaze') ? 'G-CFQ4R8LWFE' : 'G-04HWXDQBVN';
                        document.write(\`\${"<scr"}ipt async src="https://www.googletagmanager.com/gtag/js?id=\${gaId}">\${"</scr"}ipt>\`);
                        document.write(\`\${"<scr"}ipt>window.dataLayer = window.dataLayer || [];
                          function gtag(){dataLayer.push(arguments);}
                          gtag('js', new Date());
                          gtag('config', '\${gaId}', { page_path: window.location.pathname });\${"</scr"}ipt>\`);
                    `
                }} />

                <script async src="https://platform.twitter.com/widgets.js" charSet="utf-8"/>


            </Head>

            <main className={styles.main}>
                <Controller/>
            </main>

            <footer className={styles.footer}>
                <iframe
                    src="https://www.facebook.com/plugins/share_button.php?href=https%3A%2F%2Fwww.berengunsolus.com%2F&layout=button_count&size=large&appId=1809798882663411&width=88&height=28"
                    width="110" height="28" style={{border: 'none', overflow: 'hidden'}} scrolling="no" frameBorder="0"
                    allowFullScreen={true}
                    allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"/>
                <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" className="twitter-share-button"
                   data-size="large" data-text="Check out this cool puzzle game from @heptadecagon1!"
                   data-url="https://berengunsolus.com/" data-related="https://twitter.com/brazealjacob"
                   data-show-count="false">Tweet</a>
                <a
                    href="https://twitter.com/heptadecagon1"
                    style={{marginRight: '15px'}}
                    target="_blank"
                >
                    &copy; 2021 @BerenGunsolus
                </a> <span style={{color: 'gray', display: 'flex', fontSize: 'smaller'}}>h/t <a target="_blank"
                                                                                                href={"https://jacobbrazeal.com"}>@JacobBrazeal</a></span>
            </footer>
        </div>
    )
}
