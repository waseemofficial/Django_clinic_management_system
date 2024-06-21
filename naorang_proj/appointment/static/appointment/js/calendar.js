
     document.addEventListener('DOMContentLoaded', function() {
                var calendarEl = document.getElementById('calendar');

                var calendar = new FullCalendar.Calendar(calendarEl, {

                  plugins: [ 'interaction', 'dayGrid', 'timeGrid' ],

                  slotDuration: '00:20',
                  slotLabelInterval:'00:20',
                  minTime: '10:00',
                  maxTime:'20:00',
                  allDaySlot: false,
                  fixedWeekCount:false,
                  nowIndicator:true,
                  //showNonCurrentDates:false,
                  selectable: true,
                  editable:true,
                  header: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'dayGridMonth,timeGridWeek,timeGridDay'
                  },

                  businessHours: [ // specify an array instead
                      {
                        daysOfWeek: [ 1, 2, 3, 4, 6 ], // Monday, Tuesday, Wednesday, Thursday, Saturday
                        startTime: '10:00', // 8am
                        endTime: '19:00', // 6pm
                      },
                      {
                        daysOfWeek: [  5 ], //  Friday
                        startTime: '10:00', // 10am
                        endTime: '13:00', // 4pm
                      },],

                      hiddenDays: [ 7 ],

                  //calendar.addEvent(event[, ]);

                  events:events,


                  dateClick: function(info) {
                           alert('Clicked on: ' + info.dateStr);
                           alert('Coordinates: ' + info.jsEvent.pageX + ',' + info.jsEvent.pageY);
                           alert('Current view: ' + info.view.type);
                             //change the day's background color just for fun
                            info.dayEl.style.backgroundColor = 'red';
                           },
                    //});

                  eventDrop: function( info ) {
                      //write a program to update event
                      alert(info.event.title + " was dropped on " + info.event.start.toISOString());

                      if (!confirm("Are you sure about this change?")) {
                        info.revert();
                        }
                      }


                 //select: function(info) {
                  //  alert('select' +info.startStr +'to'+info.endStr);
                //  }
                });
                calendar.render();
              });
