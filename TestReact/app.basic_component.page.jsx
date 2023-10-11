
//import Picture from 'app.basic_component.picture.jsx';
/*
function Picture() {
    //const img_url = require('https://reurl.cc/L6MDD4')
    //const img_url = 'https://reurl.cc/L6MDD4'
    const img_url = "https://i.redd.it/cute-azusa-aizawa-our-new-queen-artist-pixiv-%E8%AA%B0%E5%BE%97%E3%81%A1%E3%82%83%E3%82%93-v0-asang8au6ara1.png?s=1a8eaf427a340a45c25fc340e8b6af28e34ada97"
    return (
        <div>
            <p>Azusa Aizawa (LV.99)</p>
            <img 
                src={img_url} 
                alt="Azusa Aizawa"
                width="30%"
                height="30%"
            />
        </div>
    );
}
*/

export default function Gallery() {
//function Gallery() {
    return (
        <section>
            <h1>Amazing Saga</h1>
            <Picture />
        </section>
    );
}

// 230925 : (1) use CDN and "ReactDOM" for workaround error import/export
// import { createRoot } from 'react-dom/client';
const container = document.getElementById('root');
const root = ReactDOM.createRoot(container); // createRoot(container!) if you use TypeScript
root.render(<Gallery tab="home" />);
// ReactDOM.render(<Gallery />, document.getElementById('root'));
