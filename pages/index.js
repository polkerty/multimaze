import Head from 'next/head'
import styles from '../styles/Home.module.css'
import Controller from "./controller";

import Level from './level';

export default function Home() {

    return (
        <div className={styles.container}>
            <Head>
                <title>Multimaze by Beren Gunsolus</title>
                <meta name="viewport" content="width=device-width, initial-scale=1"/>
                <link rel="icon" href="/favicon.ico"/>

                <script
                    async
                    src="https://www.googletagmanager.com/gtag/js?id=G-HGYJEPGY3W"
                />

                <script
                    dangerouslySetInnerHTML={{
                        __html: `
              window.dataLayer = window.dataLayer || [];
              function gtag(){dataLayer.push(arguments);}
              gtag('js', new Date());
              gtag('config', 'G-HGYJEPGY3W', { page_path: window.location.pathname });
            `,
                    }}
                />

            </Head>

            <main className={styles.main}>
                <Controller/>
            </main>

            <footer className={styles.footer}>
                <a
                    href="https://twitter.com/heptadecagon1"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    By @BerenGunsolus
                    {/* And @JacobBrazeal */}
                </a>
            </footer>
        </div>
    )
}
