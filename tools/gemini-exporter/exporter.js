// ==UserScript==
// @name         Gemini Memory Exporter v1.0
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Exportiert Gemini-Chats mit Markern für das Memory-System
// @author       Gemini (Architecture & Logic)
// @match        https://gemini.google.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function addExportButton() {
        if (document.getElementById('memory-export-btn')) return;

        const btn = document.createElement('button');
        btn.id = 'memory-export-btn';
        btn.innerHTML = '💾 Export for Memory';
        
        // Styling passend zum "Biest"-Vibe
        Object.assign(btn.style, {
            position: 'fixed',
            top: '15px',
            right: '250px', // Damit es nicht mit dem Account-Menü kollidiert
            zIndex: '10000',
            padding: '8px 15px',
            backgroundColor: '#1a73e8',
            color: 'white',
            border: 'none',
            borderRadius: '20px',
            cursor: 'pointer',
            fontSize: '12px',
            fontWeight: 'bold',
            boxShadow: '0 2px 5px rgba(0,0,0,0.2)'
        });

        btn.onclick = function() {
            let chatText = "";
            // Selektoren für User-Queries und Bot-Antworten
            const entries = document.querySelectorAll('.query-text, .model-response-text');

            entries.forEach(entry => {
                const text = entry.innerText.trim();
                if (text) {
                    const isUser = entry.classList.contains('query-text');
                    const marker = isUser ? "-->[USER]" : "-->[CHATBOT]";
                    chatText += `${text} ${marker}\n\n---\n\n`;
                }
            });

            if (chatText) {
                navigator.clipboard.writeText(chatText).then(() => {
                    btn.innerHTML = '✅ Copied!';
                    btn.style.backgroundColor = '#0d904f';
                    setTimeout(() => {
                        btn.innerHTML = '💾 Export for Memory';
                        btn.style.backgroundColor = '#1a73e8';
                    }, 2000);
                });
            } else {
                alert("Keine Chat-Inhalte gefunden. Sicher, dass du im Chat-Fenster bist?");
            }
        };

        document.body.appendChild(btn);
    }

    // Intervall, da Gemini eine Single-Page-App ist und Inhalte nachlädt
    setInterval(addExportButton, 2000);
})();