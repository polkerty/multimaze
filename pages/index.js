import Head from "next/head";
import styles from "../styles/Home.module.css";
import Footer from "../components/footer";
import Controller from "./controller";

function makeAnalyticsScript(id) {
  return `window.dataLayer = window.dataLayer || [];
              function gtag(){dataLayer.push(arguments);}
              gtag('js', new Date());
              gtag('config', '${id}', { page_path: window.location.pathname });`;
}

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>The Hardest Maze by Beren Gunsolus</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
        <script
          dangerouslySetInnerHTML={{
            __html: `
                        const gaId = typeof window !== 'undefined' && window.location.toString().includes('hardestmaze') ? 'G-EJCYRCMWMV' : 'G-04HWXDQBVN';
                        document.write(\`\${"<scr"}ipt async src="https://www.googletagmanager.com/gtag/js?id=\${gaId}">\${"</scr"}ipt>\`);
                        document.write(\`\${"<scr"}ipt>window.dataLayer = window.dataLayer || [];
                          function gtag(){dataLayer.push(arguments);}
                          gtag('js', new Date());
                          gtag('config', '\${gaId}', { page_path: window.location.pathname });\${"</scr"}ipt>\`);
                    `,
          }}
        />

        <script
          async
          src="https://platform.twitter.com/widgets.js"
          charSet="utf-8"
        />
      </Head>

      <main className={styles.main}>
        <Controller />
      </main>
      <Footer />
    </div>
  );
}
