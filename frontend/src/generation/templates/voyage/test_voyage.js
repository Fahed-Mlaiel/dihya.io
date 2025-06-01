import { bookTrip, createRoute } from './template';

describe('Voyage Template', () => {
  it('should create route securely', () => {
    const user = { role: 'admin' };
    const route = { destination: 'Paris' };
    expect(createRoute(route, user)).toEqual({ success: true, route });
  });

  it('should throw on invalid route', () => {
    const user = { role: 'user' };
    expect(() => createRoute({}, user)).toThrow('Invalid route');
  });

  it('should book trip securely', () => {
    const user = { role: 'user' };
    const booking = { tripId: 'TRIP123' };
    expect(bookTrip(booking, user)).toEqual({ success: true, booking });
  });

  it('should throw on unauthorized booking', () => {
    expect(() => bookTrip({ tripId: 'TRIP123' }, null)).toThrow('Unauthorized');
  });
});
