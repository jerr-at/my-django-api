import React, {useState} from "react";
import {createRoot} from "react-dom/client";
import {Heart, ShieldCheck, ArrowRight, Users, IndianRupee, Menu, X} from "lucide-react";
import "./styles.css";

const donors = [
  ["Ananya R.", "₹5,000", "Thank you for building a better tomorrow."],
  ["Rahul K.", "₹2,500", "Happy to contribute."],
  ["Priya S.", "₹1,000", "Small help, big impact."],
  ["Arun M.", "₹750", "Keep up the good work."],
  ["Meera P.", "₹500", "Glad to be part of this."],
];

function App(){
  const [page,setPage]=useState("donate");
  const [name,setName]=useState("");
  const [amount,setAmount]=useState("1000");
  const [message,setMessage]=useState("");
  const [submitted,setSubmitted]=useState(false);
  const [menu,setMenu]=useState(false);

  const submit=(e)=>{
    e.preventDefault();
    if(!name.trim() || !amount) return;
    setSubmitted(true);
  };

  return <div className="site">
    <header className="nav">
      <div className="brand"><div className="heart"><Heart size={18} fill="currentColor"/></div><span>beKind</span></div>
      <nav className={menu?"open":""}>
        <button className={page==="donate"?"active":""} onClick={()=>{setPage("donate");setMenu(false)}}>Donate</button>
        <button className={page==="wall"?"active":""} onClick={()=>{setPage("wall");setMenu(false)}}>Donor Wall</button>
      </nav>
      <button className="menu" onClick={()=>setMenu(!menu)}>{menu?<X/>:<Menu/>}</button>
    </header>

    {page==="donate" ? <main>
      <section className="hero">
        <div className="hero-copy">
          <span className="eyebrow">MAKE A DIFFERENCE</span>
          <h1>Kindness starts<br/><em>with you.</em></h1>
          <p>Your contribution helps create meaningful change. Every donation, big or small, matters.</p>
          <div className="stats">
            <div><strong>₹10,250</strong><span>raised so far</span></div>
            <div><strong>48</strong><span>kind donors</span></div>
          </div>
        </div>

        <div className="card">
          <div className="card-head"><div><h2>Make a donation</h2><p>Support the beKind community</p></div><div className="secure"><ShieldCheck size={16}/> Secure</div></div>
          {submitted ? <div className="success">
            <div className="success-icon"><Heart size={25} fill="currentColor"/></div>
            <h3>Thank you, {name}!</h3>
            <p>Your donation of ₹{Number(amount).toLocaleString("en-IN")} has been recorded.</p>
            <button onClick={()=>setSubmitted(false)}>Make another donation</button>
          </div> : <form onSubmit={submit}>
            <label>Your name<input value={name} onChange={e=>setName(e.target.value)} placeholder="Enter your name" required/></label>
            <label>Email address<input type="email" placeholder="you@example.com" required/></label>
            <label>Donation amount<div className="amount"><span>₹</span><input value={amount} onChange={e=>setAmount(e.target.value.replace(/\D/g,""))} inputMode="numeric" required/></div></label>
            <div className="quick">{["500","1000","2500","5000"].map(v=><button type="button" key={v} className={amount===v?"picked":""} onClick={()=>setAmount(v)}>₹{Number(v).toLocaleString("en-IN")}</button>)}</div>
            <label>Message <span className="optional">Optional</span><textarea value={message} onChange={e=>setMessage(e.target.value)} placeholder="Leave a note for the community"></textarea></label>
            <button className="donate" type="submit">Continue to UPI <ArrowRight size={17}/></button>
            <p className="note">Your details are securely stored and your name can appear on the donor wall.</p>
          </form>}
        </div>
      </section>
    </main> :
    <main className="wall-page">
      <section className="wall-head">
        <span className="eyebrow">OUR COMMUNITY</span>
        <h1>Donors who chose<br/><em>to be kind.</em></h1>
        <p>A live view of the people helping make a difference.</p>
        <div className="wall-total"><IndianRupee size={18}/><strong>10,250</strong><span>total contributions</span></div>
      </section>
      <section className="donor-list">
        <div className="list-title"><div><h2>Recent donors</h2><p>Thank you for making an impact.</p></div><div className="people"><Users size={16}/> 48 donors</div></div>
        {donors.map((d,i)=><div className="donor" key={i}>
          <div className="donor-avatar">{d[0][0]}</div>
          <div className="donor-info"><strong>{d[0]}</strong><span>{d[2]}</span></div>
          <b>{d[1]}</b>
        </div>)}
      </section>
    </main>}

    <footer><span>© 2025 beKind</span><span>Every contribution counts.</span></footer>
  </div>
}
createRoot(document.getElementById("root")).render(<App/>);
