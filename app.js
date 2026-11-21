const form=document.getElementById('chatForm');
const input=document.getElementById('prompt');
const messages=document.getElementById('messages');
const welcome=document.getElementById('welcome');
const send=document.getElementById('send');
let history=[];
function addMessage(text,role){if(welcome)welcome.remove();const el=document.createElement('div');el.className='message '+role;el.textContent=text;messages.appendChild(el);messages.scrollTop=messages.scrollHeight;return el;}
async function submitPrompt(text){
  const value=(text||'').trim();if(!value)return;
  input.value='';addMessage(value,'user');history.push({role:'user',content:value});
  send.disabled=true;const pending=addMessage('در حال بررسی پرسش شما…','assistant');
  try{
    const response=await fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({messages:history})});
    const data=await response.json();if(!response.ok)throw new Error(data.detail||'خطا در دریافت پاسخ');
    pending.textContent=data.reply+(data.mode==='demo'?'\n\n[حالت نمایشی]':'');history.push({role:'assistant',content:data.reply});
  }catch(e){pending.textContent='ارتباط با سرور برقرار نشد: '+e.message;history.pop();}
  finally{send.disabled=false;input.focus();messages.scrollTop=messages.scrollHeight;}
}
form.addEventListener('submit',e=>{e.preventDefault();submitPrompt(input.value)});
document.querySelectorAll('[data-prompt]').forEach(b=>b.addEventListener('click',()=>submitPrompt(b.dataset.prompt)));
document.getElementById('newChat').addEventListener('click',()=>{history=[];messages.innerHTML='';const w=document.createElement('div');w.className='welcome';w.innerHTML='<div class="welcome-mark">د</div><h1>گفت‌وگوی تازه</h1><p>پرسش حقوقی خود را بنویسید.</p>';messages.appendChild(w);});
input.addEventListener('keydown',e=>{if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();form.requestSubmit()}});
